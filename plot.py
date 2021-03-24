from argparse import ArgumentParser
import os
import uproot
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import atlas_mpl_style as ampl
from palettable.colorbrewer.qualitative import Dark2_7
ampl.use_atlas_style(usetex=False)


xlabels = {
    "DH_m": "Dark Higgs boson m [GeV]",
    "DH_pt": "Dark Higgs boson $p_{T}$ [GeV]",
    "b1_pt": "b-quark $p_{T}$ [GeV]",
    "b2_pt": "anti b-quark $p_{T}$ [GeV]",
    "met": "$E_{T}^{miss}$ [GeV]",
}

xlimits = {
    "DH_m": [30, 100],
    "DH_pt": [0, 600],
    "b1_pt": [0, 500],
    "b2_pt": [0, 500],
    "met": [0, 600],
}


def getArguments():
    parser = ArgumentParser()
    parser.add_argument("inputFile")
    parser.add_argument("--mass", help="mass of dark Higgs in GeV")
    parser.add_argument("--process", help="Name of process for legend")
    parser.add_argument(
        "--couplings",
        nargs="*",
        default=["gx_0p1", "gx_0p5", "gx_1p0", "gx_1p5", "gx_2p0", "gx_2p5", "gx_3p0", "gx_3p5"],
    )
    parser.add_argument(
        "--observables", nargs="*", default=["DH_m", "DH_pt", "b1_pt", "b2_pt", "met"]
    )
    parser.add_argument(
        "--closure",
        nargs="*",
        default=[],
    )
    return parser



def plot_ratio(
    bins, data, data_errs, bkg, bkg_errs, ratio_ax, max_ratio=None, plottype="diff", color='paper:red'
):
    """
    Plot ratio plot
    NB: :func:`atlas_mpl_style.uhi.plot_ratio` provides a version of this function that accepts ``PlottableHistogram``s.
    Parameters
    ----------
    bins : array_like
        Bin edges
    data : array_like
        Data histogram bin contents
    data_errs : array_like
        Statistical errors on data
    bkg : array_like
        Total background histogram bin contents
    bkg_errs : array_like
        Total errors on total background
    ratio_ax : mpl.axes.Axes
        Ratio axes (produced using :func:`atlas_mpl_style.ratio_axes()`)
    max_ratio : float, optional
        Maximum ratio (defaults to 0.2 for "diff", 1.2 for "raw")
    plottype : {"diff", "raw"}
        | Type of ratio to plot.
        | "diff" : (data - bkg) / bkg
        | "raw" : data / bkg
    """
    # divide by zero is common -- ignore errors
    olderr = np.seterr(all="ignore")
    if plottype == "diff":
        ratio = (data - bkg) / bkg
        if max_ratio is None:
            max_ratio = 0.2
        min_ratio = -max_ratio
    elif plottype == "raw":
        ratio = data / bkg
        if max_ratio is None:
            max_ratio = 1.2
        min_ratio = 1 - max_ratio
    else:
        raise TypeError("Invalid plottype")
    # Increase limits by 30% to avoid tick labels clashing
    max_ratio *= 1.3
    min_ratio *= 1.3

    ratio_ax.axhline(1 if plottype == "raw" else 0, color="paper:red", lw=1)
    ratio_ax.set_ylim(min_ratio, max_ratio)
    if plottype == "diff":
        ampl.plot.plot_band(
            bins, -bkg_errs / bkg, bkg_errs / bkg, color="grey", alpha=0.5, ax=ratio_ax
        )
    elif plottype == "raw":
        ampl.plot.plot_band(
            bins,
            1 - (bkg_errs / bkg),
            1 + (bkg_errs / bkg),
            color="grey",
            alpha=0.5,
            ax=ratio_ax,
        )

    bin_centers = (bins[1:] + bins[:-1]) / 2
    out_of_range_up = np.where(ratio > max_ratio, max_ratio, np.NaN)
    out_of_range_down = np.where(ratio < min_ratio, min_ratio, np.NaN)
    ratio_ax.plot(
        bin_centers,
        out_of_range_up,
        marker=mpl.markers.CARETUP,
        color=color,
        lw=0,
    )
    ratio_ax.plot(
        bin_centers,
        out_of_range_down,
        marker=mpl.markers.CARETDOWN,
        color=color,
        lw=0,
    )
    # set out of range to NaN so it doesn't get drawn
    ratio[~np.isnan(out_of_range_up)] = np.NaN
    ratio[~np.isnan(out_of_range_down)] = np.NaN
    ratio_ax.errorbar(bin_centers, ratio, yerr=(data_errs / bkg), fmt="o", ms=3, color=color)
    # re-enable errors
    np.seterr(**olderr)


def makePlot(observable, histograms, mass, process, couplings, xTitle, yTitle, outputFile, closure=None):
    # make canvas
    if closure:
        fig, ax0, ax1 = ampl.ratio_axes()
        histograms = zip([h for h in histograms], closure)
    else:
        fig, ax0 = plt.subplots()

    for i, hists in enumerate(histograms):
        if closure:
            h, h_closure = hists
            closure_values = h_closure.values()
            closure_errors = h_closure.errors()
            closure_bins = h_closure.axis().edges()
            closure_bin_centers = (closure_bins[1:] + closure_bins[:-1]) / 2
            ax0.errorbar(x=closure_bin_centers, y=closure_values, yerr=closure_errors,
                         linestyle='-', color=Dark2_7.mpl_colors[i],
                         label=couplings[i].replace('_','=').replace('p', '.') + ' (gen)')
        else:
            h = hists

        values = h.values()
        errors = h.errors()
        bins = h.axis().edges()
        bin_centers = (bins[1:] + bins[:-1]) / 2
        ax0.errorbar(x=bin_centers, y=values, yerr=errors,
                     linestyle='none', fmt='.', color=Dark2_7.mpl_colors[i],
                     label=couplings[i].replace('_','=').replace('p', '.') + ' (rwgt)')

        if closure:
            plot_ratio(closure_bins,
                values, errors,
                closure_values, closure_errors,
                ratio_ax=ax1, max_ratio=2.0, plottype="raw",
                color=Dark2_7.mpl_colors[i])
            ax1.set_xlim(left=xlimits[observable][0], right=xlimits[observable][1])
            ax1.set_ylim(bottom=0.5, top=1.5)

    ax0.set_xlim(left=xlimits[observable][0], right=xlimits[observable][1])
    ax0.set_ylim(bottom=0)

    # add labels
    ampl.plot.draw_atlas_label(0.1, 0.95)
    ampl.plot.set_ylabel('Entries', ax=ax0)
    ampl.plot.set_xlabel(xlabels[observable], ax=ax1 if closure else ax0)
    if closure: ampl.plot.set_ylabel('Ratio', ax=ax1)

    # add legend
    plt.legend(frameon=False)

    fig.savefig(outputFile)


def main():
    args = getArguments().parse_args()

    observables = {i for i in args.observables}
    couplings = args.couplings

    f = uproot.open(args.inputFile)

    # make output directory
    outDir = 'plots_' + os.path.basename(args.inputFile).replace('.root', '')
    try:
        os.makedirs(outDir)
    except OSError:
        pass
    os.chdir(outDir)

    # plot observables (1 plot per observable)
    for obs in observables:
        print(obs)
        # get histograms
        histograms = []
        for gx in couplings:
            histname = "h_{obs}_{gx}".format(obs=obs, gx=gx)
            h = f[histname]
            histograms.append(h)
        closure = []
        if args.closure:
            for fname in args.closure:
                with uproot.open(fname) as ftemp:
                    histname = "h_{obs}_nominal".format(obs=obs)
                    h = ftemp[histname]
                    closure.append(h)

        makePlot(
            obs,
            histograms,
            args.mass,
            args.process,
            args.couplings,
            xlabels[obs],
            "Events",
            obs + "_{process}_m{m}".format(process="".join(args.process.split()), m=args.mass) + ".png",
            closure,
        )

if __name__ == "__main__":
    main()
