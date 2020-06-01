
        var getData = $.get('/popvsconf');
        getData.done(function(popvsconf){
            var ctx = document.getElementById('popvsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: popvsconf.population,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(255, 0, 30)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: popvsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {
                    scales: {
                        xAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Population'
                          }
                        }],
                        yAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Confirmed Cases'
                          }
                        }]
                     }
                }
            });
        });
        var getData1 = $.get('/areavsconf');
        getData1.done(function(areavsconf){
            var ctx = document.getElementById('areavsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: areavsconf.area,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(89, 0, 255)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: areavsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {
                    scales: {
                        xAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Area'
                          }
                        }],
                        yAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Confirmed Cases'
                          }
                        }]
                     }
                }
            });
        });
        var getData2 = $.get('/denvsconf');
        getData2.done(function(denvsconf){
            var ctx = document.getElementById('denvsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: denvsconf.density,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(0, 84, 240)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: denvsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {
                    scales: {
                        xAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Density'
                          }
                        }],
                        yAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Confirmed Cases'
                          }
                        }]
                     }
                }
            });
        });

        var getData3 = $.get('/actvsconf');
        getData3.done(function(actvsconf){
            var ctx = document.getElementById('actvsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: actvsconf.active,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(0, 153, 255)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: actvsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {
                    scales: {
                        xAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Active Cases'
                          }
                        }],
                        yAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Confirmed Cases'
                          }
                        }]
                     }
                }
            });
        });

        var getData4 = $.get('/retvsconf');
        getData4.done(function(retvsconf){
            var ctx = document.getElementById('retvsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: retvsconf.retail,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(255, 34, 0)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: retvsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {
                    scales: {
                        xAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Retail Mobility'
                          }
                        }],
                        yAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Confirmed Cases'
                          }
                        }]
                     }
                }
            });
        });

        var getData5 = $.get('/grovsconf');
        getData5.done(function(grovsconf){
            var ctx = document.getElementById('grovsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: grovsconf.grocery,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(255, 191, 0)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: grovsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {
                    scales: {
                        xAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Grocery Mobility'
                          }
                        }],
                        yAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Confirmed Cases'
                          }
                        }]
                     }
                }
            });
        });

        var getData6 = $.get('/parvsconf');
        getData6.done(function(parvsconf){
            var ctx = document.getElementById('parvsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: parvsconf.parks,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(0, 115, 255)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: parvsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {
                    scales: {
                        xAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Parks Mobility'
                          }
                        }],
                        yAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Confirmed Cases'
                          }
                        }]
                     }
                }
            });
        });

        var getData7 = $.get('/stavsconf');
        getData7.done(function(stavsconf){
            var ctx = document.getElementById('stavsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: stavsconf.stations,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(247, 0, 255)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: stavsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {
                    scales: {
                        xAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Stations Mobility'
                          }
                        }],
                        yAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Confirmed Cases'
                          }
                        }]
                     }
                }
            });
        });

        var getData8 = $.get('/worvsconf');
        getData8.done(function(worvsconf){
            var ctx = document.getElementById('worvsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: worvsconf.workplaces,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(255, 0, 119)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: worvsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {
                    scales: {
                        xAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'WorkPlaces Mobility'
                          }
                        }],
                        yAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Confirmed Cases'
                          }
                        }]
                     }
                }
            });
        });
        var getData9 = $.get('/resvsconf');
        getData9.done(function(resvsconf){
            var ctx = document.getElementById('resvsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: resvsconf.residential,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(252, 152, 3)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: resvsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {
                    scales: {
                        xAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Residential Mobility'
                          }
                        }],
                        yAxes: [{
                           gridLines: {
                              display: false
                           },
                           scaleLabel: {
                            display: true,
                            labelString: 'Confirmed Cases'
                          }
                        }]
                     }
                }
            });
        });