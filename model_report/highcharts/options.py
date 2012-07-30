from model_report.highcharts.base import true, false, null, Solid, outside, undefined, _, CollectionObject, DictObject


def get_highchart_data():

    ChartData = {
        'alignTicks': true,
        'animation': true,
        'backgroundColor': "#FFFFFF",
        'borderColor': "#4572A7",
        'borderRadius': 5,
        'borderWidth': 0,
        'className': "",
        'defaultSeriesType': null,
        'events': {},
        'height': null,
        'ignoreHiddenSeries': true,
        'inverted': false,
        'margin': [null],
        'marginTop': null,
        'marginRight': 0,
        'marginBottom': 0,
        'marginLeft': 80,
        'plotBackgroundColor': null,
        'plotBackgroundImage': null,
        'plotBorderColor': "#C0C0C0",
        'plotBorderWidth': 0,
        'plotShadow': false,
        'reflow': true,
        'renderTo': null,
        'resetZoomButton': {},
        # 'selectionMarkerFill': rgba(69, 114, 167, 0.25),
        'shadow': false,
        'showAxes': false,
        'spacingTop': 10,
        'spacingRight': 10,
        'spacingBottom': 15,
        'spacingLeft': 10,
        'style': {},
        'type': "line",
        'width': null,
        'zoomType': ""
    }

    CreditsData = {
        'enabled': false
    }

    TitleData = {
        'align': "center",
        'floating': false,
        'margin': 15,
        'text': null,
        'style': {},
        'verticalAlign': "top",
        'x': 15,
        'y': 15
    }

    SubtitleData = {
        'align': "center",
        'floating': false,
        'text': "",
        'style': {},
        'verticalAlign': "top",
        'x': 0,
        'y': 30
    }

    #Solid = 'Solid'
    #outside = 'outside'
    #undefined = 'undefined'

    xAxisData = {
        'allowDecimals': true,
        'alternateGridColor': null,
        'categories': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'dateTimeLabelFormats': null,
        'endOnTick': false,
        'events': {},
        'gridLineColor': "#C0C0C0",
        'gridLineDashStyle': Solid,
        'gridLineWidth': 0,
        'id': null,
        'labels': {},
        'lineColor': "#C0D0E0",
        'lineWidth': 1,
        'linkedTo': null,
        'max': null,
        'maxPadding': 0.01,
        'maxZoom': null,
        'min': null,
        'minorGridLineColor': '#E0E0E0',
        'minorGridLineDashStyle': Solid,
        'minorGridLineWidth': 1,
        'minorTickColor': '#A0A0A0',
        'minorTickInterval': null,
        'minorTickLength': 2,
        'minorTickPosition': outside,
        'minorTickWidth': 0,
        'minPadding': 0.01,
        'minRange': null,
        'offset': 0,
        'opposite': false,
        'plotBands': [{}],
        'plotLines': [{}],
        'reversed': false,
        'showFirstLabel': true,
        'showLastLabel': false,
        'startOfWeek': 1,
        'startOnTick': false,
        'tickColor': '#C0D0E0',
        'tickInterval': null,
        'tickLength': 5,
        'tickmarkPlacement': "between",
        'tickPixelInterval': null,
        'tickPosition': "outside",
        'tickWidth': 1,
        'title': {},
        'type': "linear"
    }

    yAxisData = {
        'endOnTick': true,
        'gridLineWidth': 1,
        'lineWidth': 0,
        'maxPadding': 0.05,
        'minPadding': 0.05,
        'showLastLabel': true,
        'stackLabels': {},
        'startOnTick': true,
        'tickWidth': 0,
        'allowDecimals': true,
        'alternateGridColor': null,
        'categories': [],
        'dateTimeLabelFormats': null,
        'events': {},
        'gridLineColor': "#C0C0C0",
        'gridLineDashStyle': Solid,
        'id': null,
        'labels': {},
        'lineColor': "#C0D0E0",
        'linkedTo': null,
        'max': null,
        'maxZoom': null,
        'min': null,
        'minorGridLineColor': '#E0E0E0',
        'minorGridLineDashStyle': Solid,
        'minorGridLineWidth': 1,
        'minorTickColor': '#A0A0A0',
        'minorTickInterval': null,
        'minorTickLength': 2,
        'minorTickPosition': outside,
        'minorTickWidth': 0,
        'minRange': null,
        'offset': 0,
        'opposite': false,
        'plotBands': [{}],
        'plotLines': [{
            'value': 0,
            'width': 1,
            'color': '#808080'
        }],
        'reversed': false,
        'showFirstLabel': true,
        'startOfWeek': 1,
        'tickColor': '#C0D0E0',
        'tickInterval': null,
        'tickLength': 5,
        'tickmarkPlacement': "between",
        'tickPixelInterval': null,
        'tickPosition': "outside",
        'title': {
            'text': 'Subtitle'
        },
        'type': "linear"
    }

    TooltipData = {
        'backgroundColor': "rgba(255, 255, 255, .85)",
        'borderColor': "auto",
        'borderRadius': 5,
        'borderWidth': 2,
        'crosshairs': null,
        'enabled': true,
        'footerFormat': false,
        'formatter': "function() { return '<b>'+ this.series.name + '</b><br/>' + this.x + ': ' + this.y +'C'; }",
        'pointFormat': null,
        'positioner': null,
        'shadow': true,
        'shared': false,
        'snap': 10 / 25,
        'style': {},
        'valueDecimals': null,
        'valuePrefix': "",
        'valueSuffix': "",
        'xDateFormat': null,
        'useHTML': false
    }

    SeriesData = {
        'data': [],
        'dataParser': null,
        'dataURL': null,
        'legendIndex': undefined,
        'name': '',
        'stack': null,
        'type': "line",
        'xAxis': 0,
        'yAxis': 0
    }

    SeriesCollection = CollectionObject

    plotOptionsDataPIE_Labels = {
        'align': null,
        'connectorWidth': 1,
        'connectorColor': "{point.color}",
        'connectorPadding': 5,
        'distance': 30,
        'enabled': true,
        'softConnector': true,
        'backgroundColor': undefined,
        'borderColor': undefined,
        'borderRadius': 0,
        'borderWidth': 0,
        'color': null,
        'formatter': "",
        'padding': 2,
        'rotation': 0,
        'shadow': false,
        'staggerLines': "",
        'step': "",
        'style': {},
        'x': 0,
        'y': -6,
        'overflow': undefined
    }

    plotOptionsDataPIE = {
        'borderColor': "#FFFFFF",
        'borderWidth': 1,
        'center': ['50%', '50%'],
        'innerSize': 0,
        'showInLegend': false,
        'size': "75%",
        'slicedOffset': 10,
        'allowPointSelect': false,
        'animation': true,
        'color': "#000000",
        'connectNulls': false,
        'cropThreshold': 300,
        'cursor': '',
        'dashStyle': null,
        'dataLabels': DictObject(**plotOptionsDataPIE_Labels),
        'enableMouseTracking': true,
        'events': {},
        'id': null,
        'lineWidth': 2,
        'marker': {},
        'point': {},
        'pointStart': 0,
        'pointInterval': 1,
        'selected': false,
        'shadow': true,
        'showCheckbox': false,
        'stacking': null,
        'states': {},
        'stickyTracking': true,
        'tooltip': {},
        'turboThreshold': 1000,
        'visible': true,
        'zIndex': null
    }

    plotOptionsData = {
        'area': {},
        'areaspline': {},
        'bar': {},
        'column': {},
        'line': {},
        'pie': DictObject(**plotOptionsDataPIE),
        'series': [{}],
        'scatter': {},
        'spline': {}
    }

    legendData = {
        'align': "center",
        'backgroundColor': null,
        'borderColor': '#909090',
        'borderRadius': 5,
        'borderWidth': 1,
        'enabled': true,
        'floating': false,
        'itemHiddenStyle': {},
        'itemHoverStyle': {},
        'itemMarginBottom': 0,
        'itemMarginTop': 0,
        'itemStyle': {},
        'itemWidth': null,
        'layout': "horizontal",
        'labelFormatter': null,
        'lineHeight': 16,
        'margin': 15,
        'navigation': {},
        'padding': 8,
        'reversed': false,
        'rtl': false,
        'shadow': false,
        'style': {},
        'symbolPadding': 5,
        'symbolWidth': 30,
        'verticalAlign': "bottom",
        'width': null,
        'x': 0,
        'y': 0
    }

    langData = {
        'decimalPoint': ".",
        'downloadPNG': _("Download PNG image"),
        'downloadJPEG': _("Download JPEG image"),
        'downloadPDF': _("Download PDF document"),
        'downloadSVG': _("Download SVG vector image"),
        'exportButtonTitle': _("Export to raster or vector image"),
        'loading': _('Loading...'),
        'months': [_('January'), _('February'), _('March'), _('April'), _('May'), _('June'), _('July'), _('August'), _('September'), _('October'), _('November'), _('December')],
        'shortMonths': [_('Jan'), _('Feb'), _('Mar'), _('Apr'), _('May'), _('Jun'), _('Jul'), _('Aug'), _('Sep'), _('Oct'), _('Nov'), _('Dec')],
        'printButtonTitle': _("Print the chart"),
        'resetZoom': _('Reset zoom'),
        'resetZoomTitle': _('Reset zoom level 1:1'),
        'thousandsSep': ",",
        'weekdays': [_('Sunday'), _('Monday'), _('Tuesday'), _('Wednesday'), _('Thursday'), _('Friday'), _('Saturday')]
    }

    HighchartData = dict(
        credits=DictObject(**CreditsData),
        chart=DictObject(**ChartData),
        title=DictObject(**TitleData),
        subtitle=DictObject(**SubtitleData),
        xAxis=DictObject(**xAxisData),
        yAxis=DictObject(**yAxisData),
        tooltip=DictObject(**TooltipData),
        series=SeriesCollection(),
        plotOptions=DictObject(**plotOptionsData),
        legend=DictObject(**legendData),
        lang=DictObject(**langData),
        serie_obj=DictObject(**SeriesData),
    )

    return HighchartData
