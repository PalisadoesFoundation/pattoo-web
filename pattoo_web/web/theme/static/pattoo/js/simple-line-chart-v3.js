
  function SimpleLineChart( url, heading ) {
    //
    // This script creates the charts for customer cabinet power and bandwidth data
    //
    // Args:
    //  url: URL from which to retrieve JSON data
    //  heading: Heading for chart
    //
    // Initialise key variables
    var margin = {top: 20, right: 250, bottom: 50, left: 50};
    var headingVOffset = 0;
    var outerWidth = 1050;
    var outerHeight = 400;
    var div_id = 'pattoo-simple-line-chart'
    var innerWidth = outerWidth - margin.left - margin.right;
    var innerHeight = outerHeight - margin.top - margin.bottom;

    var legendBoxSize = 10;
    var legendStartYAxis = outerHeight - margin.bottom - margin.top - legendBoxSize;

    // Setup standard colors
    var standard_colors = d3.scaleOrdinal(d3.schemeCategory10);

    // Define the limits of the SVG canvas
    var svg = d3.select(div_id).append('svg')
      .attr('width', outerWidth)
      .attr('height', outerHeight);

    // Define the graph area on the canvas
    var g = svg.append('g')
      .attr('transform', 'translate(' + margin.left + ', ' + margin.top + ')');

    // Set scales and colors for chart area
    var x = d3.scaleTime().range([0, innerWidth]),
        y = d3.scaleLinear().range([innerHeight, 0]);

    // Set the dimensions of the canvas / graph
    // var margin = {top: 30, right: 20, bottom: 30, left: 50},
    //    width = 600 - margin.left - margin.right,
    //    height = 270 - margin.top - margin.bottom;

    // Set the ranges
    // var x = d3.time.scale().range([0, width]);
    // var y = d3.scale.linear().range([height, 0]);

    // Define the axes
    var xAxis = d3.svg.axis().scale(x)
        .orient("bottom").ticks(5);

    var yAxis = d3.svg.axis().scale(y)
        .orient("left").ticks(5);

    // Define the line
    var valueline = d3.line()
        .x(function(d) { return x(d.timestamp); })
        .y(function(d) { return y(d.value); });

    d3.json(url, function(error, data) {
       data.forEach(function(d) {
            d.timestamp = new Date(d.timestamp * 1000);
            d.value = +d.value;
        });

        // Scale the range of the data
        x.domain(d3.extent(data, function(d) { return d.timestamp; }));
        y.domain([0, d3.max(data, function(d) { return d.value; })]);

        // Add the valueline path.
        svg.append("path")
            .attr("class", "line")
            .attr("d", valueline(data));

        // Add the X Axis
        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis);

        // Add the Y Axis
        svg.append("g")
            .attr("class", "y axis")
            .call(yAxis);

    });

  }
