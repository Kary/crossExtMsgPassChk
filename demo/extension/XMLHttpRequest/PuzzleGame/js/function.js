'use strict';


function newGame() {
	reset();
	genNum();
} // function newGame()


function goUp() {
	// from row #5 to #1
	for (let i = 1; i < 6; i++) { // for column #1 to #5
		let iStr = i.toString()

		let c1X = logGrid[("c1" + iStr)];
		let c2X = logGrid[("c2" + iStr)];
		let c3X = logGrid[("c3" + iStr)];
		let c4X = logGrid[("c4" + iStr)];
		let c5X = logGrid[("c5" + iStr)];

		// -- 2 --
		if (c2X != 0) {

			if (c1X != 0) {

				if (c3X != 0) {

					if (c4X != 0) {

						// "X", "X", "X", "X", "X"
						if (c5X != 0) {

							if (c1X == c2X) { // Check If Same Num
								if (c3X == c4X) { // Check If Same Num
									c1X = c1X * 2;
									c2X = c3X * 2;
									c3X = c5X;
									c4X = 0;
									c5X = 0;
								} else if (c4X == c5X) { // Check If Same Num
									c1X = c1X * 2;
									c2X = c3X;
									c3X = c4X * 2;
									c4X = 0;
									c5X = 0;
								}
								else {
									c1X = c1X * 2;
									c2X = c3X;
									c3X = c4X;
									c4X = c5X;
									c5X = 0;
								}
							} else if (c2X == c3X) { // Check If Same Num
								if (c4X == c5X) { // Check If Same Num
									// do nth for c1X
									c2X = c2X * 2;
									c3X = c4X * 2;
									c4X = 0;
									c5X = 0;
								} else {
									// do nth for c1X
									c2X = c2X * 2;
									c3X = c4X;
									c4X = c5X;
									c5X = 0;
								}
							} else if (c3X == c4X) { // Check If Same Num
								// do nth for c1X & c2X
								c3X = c3X * 2;
								c4X = c5X;
								c5X = 0;
							} else if (c4X == c5X) { // Check If Same Num
								// do nth for c1X, c2X & c3X
								c4X = c4X * 2;
								c5X = 0;
							} else {
								// do nth
							}

						// "X", "X", "X", "X", " "
						} else {
							if (c1X == c2X) { // Check If Same Num
								if (c3X == c4X) { // Check If Same Num
									c1X = c1X * 2;
									c2X = c3X * 2;
									c3X = 0;
									c4X = 0;
								} else {
									c1X = c1X * 2;
									c2X = c3X;
									c3X = c4X;
									c4X = 0;
								}
							} else if (c2X == c3X) { // Check If Same Num
								// do nth for c1X
								c2X = c2X * 2;
								c3X = c4X;
								c4X = 0;
							} else if (c3X == c4X) { // Check If Same Num
								// do nth for c1X & c2X
								c3X = c3X * 2;
								c4X = 0;
							} else {
								// do nth
							}	
						}

					} else {
						// "X", "X", "X", " ", "X"
						if (c5X != 0) {

							if (c1X == c2X) { // Check If Same Num
								if (c3X == c5X) { // Check If Same Num
									c1X = c1X * 2;
									c2X = c3X * 2;
									c3X = 0;
									c5X = 0;
								} else {
									c1X = c1X * 2;
									c2X = c3X;
									c3X = c5X;
									c5X = 0;
								}
							} else if (c2X == c3X) { // Check If Same Num
								// do nth for c1X
								c2X = c2X * 2;
								c3X = c5X;
								c5X = 0;
							} else if (c3X == c5X) { // Check If Same Num
								// do nth for c1X & c2X
								c3X = c3X * 2;
								c5X = 0;
							} else {
								// do nth for c1X, c2X & c3X
								c4X = c5X;
								c5X = 0;
							}

						// "X", "X", "X", " ", " "
						} else {
							if (c1X == c2X) { // Check If Same Num
								c1X = c1X * 2;
								c2X = c3X;
								c3X = 0;
							} else if (c2X == c3X) { // Check If Same Num
								// do nth for c1X
								c2X = c2X * 2;
								c3X = 0;
							} else {
								// do nth
							}
						}
					}

				} else {
					if (c4X != 0) {

						// "X", "X", " ", "X", "X"
						if (c5X != 0) {
							
							if (c1X == c2X) { // Check If Same Num
								if (c4X == c5X) { // Check If Same Num
									c1X = c1X * 2;
									c2X = c4X * 2;
									c4X = 0;
									c5X = 0;
								} else {
									c1X = c1X * 2;
									c2X = c4X;
									c3X = c5X;
									c4X = 0;
									c5X = 0;
								}
							} else if (c2X == c4X) { // Check If Same Num
								// do nth for c1X
								c2X = c2X * 2;
								c3X = c5X;
								c4X = 0;
								c5X = 0;
							} else if (c4X == c5X) { // Check If Same Num
								// do nth for c1X & c2X
								c3X = c4X * 2;
								c4X = 0;
								c5X = 0;
							} else {
								// do nth for c1X & c2X
								c3X = c4X;
								c4X = c5X;
								c5X = 0;
							}

						// "X", "X", " ", "X", " "
						} else {
							if (c1X == c2X) { // Check If Same Num
								c1X = c1X * 2;
								c2X = c4X;
								c4X = 0;
							} else if (c2X == c4X) { // Check If Same Num
								// do nth for c1X
								c2X = c2X * 2;
								c4X = 0;
							}
							else {
								// do nth for c1X & c2X
								c3X = c4X;
								c4X = 0;
							}	
						}

					} else { 
						// "X", "X", " ", " ", "X"
						if (c5X != 0) {

							if (c1X == c2X) { // Check If Same Num
								c1X = c1X * 2;
								c2X = c5X;
								c5X = 0;
							} else if (c2X == c5X) { // Check If Same Num
								// do nth for c1X
								c2X = c2X * 2;
								c5X = 0;
							} else {
								// do nth for c1X & c2X
								c3X = c5X;
								c5X = 0;
							}

						// "X", "X", " ", " ", " "
						} else {
							if (c1X == c2X) { // Check If Same Num
								c1X = c1X * 2;
								c2X = 0;
							} else {
								// do nth
							}
						}
					}
				}

			} else {
				if (c3X != 0) {

					if (c4X != 0) {

						// " ", "X", "X", "X", "X"
						if (c5X != 0) {

							if (c2X == c3X) { // Check If Same Num
								if (c4X == c5X) { // Check If Same Num
									c1X = c2X * 2;
									c2X = c4X * 2;
									c3X = 0;
									c4X = 0;
									c5X = 0;
								} else {
									c1X = c2X * 2;
									c2X = c4X;
									c3X = c5X;
									c4X = 0;
									c5X = 0;
								}
							} else if (c3X == c4X) { // Check If Same Num
								c1X = c2X;
								c2X = c3X * 2;
								c3X = c5X;
								c4X = 0;
								c5X = 0;
							} else if (c4X == c5X) { // Check If Same Num
								c1X = c2X;
								c2X = c3X;
								c3X = c4X * 2;
								c4X = 0;
								c5X = 0;
							} else {
								c1X = c2X;
								c2X = c3X;
								c3X = c4X;
								c4X = c5X;
								c5X = 0;
							}

						// " ", "X", "X", "X", " "
						} else {
							if (c2X == c3X) { // Check If Same Num
								c1X = c2X * 2;
								c2X = c4X;
								c3X = 0;
								c4X = 0;
							} else if (c3X == c4X) { // Check If Same Num
								c1X = c2X;
								c2X = c3X * 2;
								c3X = 0;
								c4X = 0;
							} else {
								c1X = c2X;
								c2X = c3X;
								c3X = c4X;
								c4X = 0;
							}
						}

					} else {
						// " ", "X", "X", " ", "X"
						if (c5X != 0) {

							if (c2X == c3X) { // Check If Same Num
								c1X = c2X * 2;
								c2X = c5X;
								c3X = 0;
								c5X = 0;
							} else if (c3X == c5X) { // Check If Same Num
								c1X = c2X;
								c2X = c3X * 2;
								c3X = 0;
								c5X = 0;
							} else {
								c1X = c2X;
								c2X = c3X;
								c3X = c5X;
								c5X = 0;
							}

						// " ", "X", "X", " ", " "
						} else {
							if (c2X == c3X) { // Check If Same Num
								c1X = c2X * 2;
								c2X = 0;
								c3X = 0;
							} else {
								c1X = c2X;
								c2X = c3X;
								c3X = 0;
							}
						}
					}

				} else {
					if (c4X != 0) {

						// " ", "X", " ", "X", "X"
						if (c5X != 0) {

							if (c2X == c4X) { // Check If Same Num
								c1X = c2X * 2;
								c2X = c5X;
								c4X = 0;
								c5X = 0;
							} else if (c4X == c5X) { // Check If Same Num
								c1X = c2X;
								c2X = c4X * 2;
								c4X = 0;
								c5X = 0;
							} else {
								c1X = c2X;
								c2X = c4X;
								c3X = c5X;
								c4X = 0;
								c5X = 0;
							}

						// " ", "X", " ", "X", " "
						} else {
							if (c2X == c4X) { // Check If Same Num
								c1X = c2X * 2;
								c2X = 0;
								c4X = 0;
							} else {
								c1X = c2X;
								c2X = c4X;
								c4X = 0;
							}
						}

					} else {
						// " ", "X", " ", " ", "X"
						if (c5X != 0) {

							if (c2X == c5X) { // Check If Same Num
								c1X = c2X * 2;
								c2X = 0;
								c5X = 0;
							} else {
								c1X = c2X;
								c2X = c5X;
								c5X = 0;
							}	

						// " ", "X", " ", " ", " "
						} else {
							c1X = c2X;
							c2X = 0;
						}
					}
				}
			}

		// -- 3 --
		} else if (c3X != 0) {

			if (c1X != 0) {

				if (c4X != 0) {

					// "X", " ", "X", "X", "X"
					if (c5X != 0) {

						if (c1X == c3X) { // Check If Same Num
							if (c4X == c5X) { // Check If Same Num
								c1X = c1X * 2;
								c2X = c4X * 2;
								c3X = 0;
								c4X = 0;
								c5X = 0;
							} else {
								c1X = c1X * 2;
								c2X = c4X;
								c3X = c5X;
								c4X = 0;
								c5X = 0;
							}
						} else if (c3X == c4X) { // Check If Same Num
							// do nth for c1X
							c2X = c3X * 2;
							c3X = c5X;
							c4X = 0;
							c5X = 0;
						} else if (c4X == c5X) { // Check If Same Num
							// do nth for c1X
							c2X = c3X;
							c3X = c4X * 2;
							c4X = 0;
							c5X = 0;
						} else {
							// do nth for c1X
							c2X = c3X;
							c3X = c4X;
							c4X = c5X;
							c5X = 0;
						}

					// "X", " ", "X", "X", " "
					} else {
						if (c1X == c3X) { // Check If Same Num
							c1X = c1X * 2;
							c2X = c4X;
							c3X = 0;
							c4X = 0;
						} else if (c3X == c4X) { // Check If Same Num
							// do nth for c1X
							c2X = c3X * 2;
							c3X = 0;
							c4X = 0;
						} else {
							// do nth for c1X
							c2X = c3X;
							c3X = c4X;
							c4X = 0;
						}	
					}

				} else {
					// "X", " ", "X", " ", "X"
					if (c5X != 0) {

						if (c1X == c3X) { // Check If Same Num
							c1X = c1X * 2;
							c2X = c5X;
							c3X = 0;
							c5X = 0;
						} else if (c3X == c5X) { // Check If Same Num
							// do nth for c1X
							c2X = c3X * 2;
							c3X = 0;
							c5X = 0;
						} else {
							// do nth for c1X
							c2X = c3X;
							c3X = c5X;
							c5X = 0;
						}

					// "X", " ", "X", " ", " "
					} else {
						if (c1X == c3X) { // Check If Same Num
							c1X = c1X * 2;
							c3X = 0;
						} else {
							// do nth for c1X
							c2X = c3X;
							c3X = 0;
						}
					}
				}

			} else {
				if (c4X != 0) {

					// " ", " ", "X", "X", "X"
					if (c5X != 0) {

						if (c3X == c4X) { // Check If Same Num
							c1X = c3X * 2;
							c2X = c5X;
							c3X = 0;
							c4X = 0;
							c5X = 0;
						} else if (c4X == c5X) { // Check If Same Num
							c1X = c3X;
							c2X = c4X * 2;
							c3X = 0;
							c4X = 0;
							c5X = 0;
						} else {
							c1X = c3X;
							c2X = c4X;
							c3X = c5X;
							c4X = 0;
							c5X = 0;
						}
					
					// " ", " ", "X", "X", " "
					} else {
						if (c3X == c4X) { // Check If Same Num
							c1X = c3X * 2;
							c3X = 0;
							c4X = 0;
						} else {
							c1X = c3X;
							c2X = c4X;
							c3X = 0;
							c4X = 0;
						}
					}
					
				} else {
					// " ", " ", "X", " ", "X"
					if (c5X != 0) {

						if (c3X == c5X) { // Check If Same Num
							c1X = c3X * 2;
							c3X = 0;
							c5X = 0;
						} else {
							c1X = c3X;
							c2X = c5X;
							c3X = 0;
							c5X = 0;
						}

					// " ", " ", "X", " ", " "
					} else {
						c1X = c3X;
						c3X = 0;
					}
				}
			}

		// -- 4 --
		} else if (c4X != 0) {

			if (c1X != 0) {

				// "X", " ", " ", "X", "X"
				if (c5X != 0) {

					if (c1X == c4X) { // Check If Same Num
						c1X = c1X * 2;
						c2X = c5X;
						c4X = 0;
						c5X = 0;
					} else if (c4X == c5X) { // Check If Same Num
						// do nth for c1X
						c2X = c4X * 2;
						c4X = 0;
						c5X = 0;
					} else {
						// do nth for c1X
						c2X = c4X;
						c3X = c5X;
						c4X = 0;
						c5X = 0;
					}

				// "X", " ", " ", "X", " "
				} else {
					if (c1X == c4X) { // Check If Same Num
						c1X = c1X * 2;
						c4X = 0;
					} else {
						// do nth for c1X
						c2X = c4X;
						c4X = 0;
					}
				}

			} else {
				// " ", " ", " ", "X", "X"
				if (c5X != 0) {

					if (c4X == c5X) { // Check If Same Num
						c1X = c4X * 2;
						c4X = 0;
						c5X = 0;
					} else {
						c1X = c4X;
						c2X = c5X;
						c4X = 0;
						c5X = 0;
					}

				// " ", " ", " ", "X", " "
				} else {
					c1X = c4X;
					c4X = 0;
				}
			}

		// -- 5 --
		} else if (c5X != 0) {

			// "X", " ", " ", " ", "X"
			if (c1X != 0) {

				if (c1X == c5X) { // Check If Same Num
					c1X = c1X * 2;
					c5X = 0;
				} else {
					// do nth for c1X
					c2X = c5X;
					c5X = 0;
				}

			// " ", " ", " ", " ", "X"
			} else {
				c1X = c5X;
				c5X = 0;
			}

		} else {
			// do nth
		}

		logGrid[("c1" + iStr)] = c1X;
		logGrid[("c2" + iStr)] = c2X;
		logGrid[("c3" + iStr)] = c3X;
		logGrid[("c4" + iStr)] = c4X;
		logGrid[("c5" + iStr)] = c5X;
	}
} // function goUp()


function goDown() {
	// from row #1 to #5
	for (let i = 1; i < 6; i++) { // for column #1 to #5
		let iStr = i.toString()

		let c1X = logGrid[("c1" + iStr)];
		let c2X = logGrid[("c2" + iStr)];
		let c3X = logGrid[("c3" + iStr)];
		let c4X = logGrid[("c4" + iStr)];
		let c5X = logGrid[("c5" + iStr)];

		// -- 4 --
		if (c4X != 0) {
			
			if (c5X != 0) {

				if (c3X != 0) {

					if (c2X != 0) {

						// "X", "X", "X", "X", "X"
						if (c1X != 0) {

							if (c5X == c4X) { // Check If Same Num
								if (c3X == c2X) { // Check If Same Num
									c5X = c5X * 2;
									c4X = c3X * 2;
									c3X = c1X;
									c2X = 0;
									c1X = 0;
								} else if (c2X == c1X) { // Check If Same Num
									c5X = c5X * 2;
									c4X = c3X;
									c3X = c2X * 2;
									c2X = 0;
									c1X = 0;
								} else {
									c5X = c5X * 2;
									c4X = c3X;
									c3X = c2X;
									c2X = c1X;
									c1X = 0;
								}
							} else if (c4X == c3X) { // Check If Same Num
								if (c2X == c1X) { // Check If Same Num
									// do nth for c5X
									c4X = c4X * 2;
									c3X = c2X * 2;
									c2X = 0;
									c1X = 0;
								} else {
									// do nth for c5X
									c4X = c4X * 2;
									c3X = c2X;
									c2X = c1X;
									c1X = 0;
								}
							} else if (c3X == c2X) { // Check If Same Num
								// do nth for c5X & c4X
								c3X = c3X * 2;
								c2X = c1X;
								c1X = 0;
							} else if (c2X == c1X) { // Check If Same Num
								// do nth for c5X, c4X & c3X
								c2X = c2X * 2;
								c1X = 0;
							} else {
								// do nth
							}

						// " ", "X", "X", "X", "X"
						} else {
							if (c5X == c4X) { // Check If Same Num
								if (c3X == c2X) { // Check If Same Num
									c5X = c5X * 2;
									c4X = c3X * 2;
									c3X = 0;
									c2X = 0;
								} else {
									c5X = c5X * 2;
									c4X = c3X;
									c3X = c2X;
									c2X = 0;
								}
							} else if (c4X == c3X) { // Check If Same Num
								// do nth for c5X
								c4X = c4X * 2;
								c3X = c2X;
								c2X = 0;
							} else if (c3X == c2X) { // Check If Same Num
								// do nth for c5X & c4X
								c3X = c3X * 2;
								c2X = 0;
							} else {
								// do nth
							}
						}

					} else {
						// "X", " ", "X", "X", "X"
						if (c1X != 0) {

							if (c5X == c4X) { // Check If Same Num
								if (c3X == c1X) { // Check If Same Num
									c5X = c5X * 2;
									c4X = c3X * 2;
									c3X = 0;
									c1X = 0;
								} else {
									c5X = c5X * 2;
									c4X = c3X;
									c3X = c1X;
									c1X = 0;
								}
							} else if (c3X == c4X) { // Check If Same Num
								// do nth for c5X
								c4X = c4X * 2;
								c3X = c1X;
								c1X = 0;
							} else if (c3X == c1X) { // Check If Same Num
								// do nth for c5X & c4X
								c3X = c3X * 2;
								c1X = 0;
							} else {
								// do nth for c5X, c4X & c3X
								c2X = c1X;
								c1X = 0;
							}

						// " ", " ", "X", "X", "X"
						} else {
							if (c5X == c4X) { // Check If Same Num
								c5X = c5X * 2;
								c4X = c3X;
								c3X = 0;
							} else if (c3X == c4X) { // Check If Same Num
								// do nth for c5X
								c4X = c4X * 2;
								c3X = 0;
							} else {
								// do nth
							}
						}
					}

				} else {
					if (c2X != 0) {

						// "X", "X", " ", "X", "X"
						if (c1X != 0) {

							if (c5X == c4X) { // Check If Same Num
								if (c2X == c1X) { // Check If Same Num
									c5X = c5X * 2;
									c4X = c2X * 2;
									c2X = 0;
									c1X = 0;
								} else {
									c5X = c5X * 2;
									c4X = c2X;
									c3X = c1X;
									c2X = 0;
									c1X = 0;
								}
							} else if (c2X == c4X) { // Check If Same Num
								// do nth for c5X
								c4X = c4X * 2;
								c3X = c1X;
								c2X = 0;
								c1X = 0;
							} else if (c2X == c1X) { // Check If Same Num
								// do nth for c5X & c4X
								c3X = c2X * 2;
								c2X = 0;
								c1X = 0;
							} else {
								// do nth for c5X & c4X
								c3X = c2X;
								c2X = c1X;
								c1X = 0;
							}

						// " ", "X", " ", "X", "X"
						} else {
							if (c5X == c4X) { // Check If Same Num
								c5X = c5X * 2;
								c4X = c2X;
								c2X = 0;
							} else if (c2X == c4X) { // Check If Same Num
								// do nth for c5X
								c4X = c4X * 2;
								c2X = 0;
							} else {
								// do nth for c5X & c4X
								c3X = c2X;
								c2X = 0;
							}
						}

					} else {
						// "X", " ", " ", "X", "X"
						if (c1X != 0) {

							if (c5X == c4X) { // Check If Same Num
								c5X = c5X * 2;
								c4X = c1X;
								c1X = 0;
							} else if (c1X == c4X) { // Check If Same Num
								// do nth for c5X
								c4X = c4X * 2;
								c1X = 0;
							} else {
								// do nth for c4X & c5X
								c3X = c1X;
								c1X = 0;
							}

						// " ", " ", " ", "X", "X"
						} else {
							if (c5X == c4X) { // Check If Same Num
								c5X = c5X * 2;
								c4X = 0;
							} else {
								// do nth
							}
						}
					}
				}

			} else {
				if (c3X != 0) {

					if (c2X != 0) {

						// "X", "X", "X", "X", " "
						if (c1X != 0) {

							if (c3X == c4X) { // Check If Same Num
								if (c2X == c1X) { // Check If Same Num
									c5X = c4X * 2;
									c4X = c2X * 2;
									c3X = 0;
									c2X = 0;
									c1X = 0;
								} else {
									c5X = c4X * 2;
									c4X = c2X;
									c3X = c1X;
									c2X = 0;
									c1X = 0;
								}
							} else if (c3X == c2X) { // Check If Same Num
								c5X = c4X;
								c4X = c3X * 2;
								c3X = c1X;
								c2X = 0;
								c1X = 0;
							} else if (c2X == c1X) { // Check If Same Num
								c5X = c4X;
								c4X = c3X;
								c3X = c2X * 2;
								c2X = 0;
								c1X = 0;
							} else {
								c5X = c4X;
								c4X = c3X;
								c3X = c2X;
								c2X = c1X;
								c1X = 0;
							}

						// " ", "X", "X", "X", " "
						} else {
							if (c3X == c4X) { // Check If Same Num
								c5X = c4X * 2;
								c4X = c2X;
								c3X = 0;
								c2X = 0;
							} else if (c3X == c2X) { // Check If Same Num
								c5X = c4X;
								c4X = c3X * 2;
								c3X = 0;
								c2X = 0;
							} else {
								c5X = c4X;
								c4X = c3X;
								c3X = c2X;
								c2X = 0;
							}
						}

					} else {
						// "X", " ", "X", "X", " "
						if (c1X != 0) {

							if (c3X == c4X) { // Check If Same Num
								c5X = c4X * 2;
								c4X = c1X;
								c3X = 0;
								c1X = 0;
							} else if (c1X == c3X) { // Check If Same Num
								c5X = c4X;
								c4X = c3X * 2;
								c3X = 0;
								c1X = 0;
							} else {
								c5X = c4X;
								c4X = c3X;
								c3X = c1X;
								c1X = 0;							}

						// " ", " ", "X", "X", " "
						} else {
							if (c3X == c4X) { // Check If Same Num
								c5X = c4X * 2;
								c4X = 0;
								c3X = 0;
							} else {
								c5X = c4X;
								c4X = c3X;
								c3X = 0;
							}
						}
					}

				} else {
					if (c2X != 0) {

						// "X", "X", " ", "X", " "
						if (c1X != 0) {

							if (c2X == c4X) { // Check If Same Num
								c5X = c4X * 2;
								c4X = c1X;
								c2X = 0;
								c1X = 0;
							} else if (c2X == c1X) { // Check If Same Num
								c5X = c4X;
								c4X = c2X * 2;
								c2X = 0;
								c1X = 0;
							} else {
								c5X = c4X;
								c4X = c2X;
								c3X = c1X;
								c2X = 0;
								c1X = 0;
							}

						// " ", "X", " ", "X", " "
						} else {
							if (c2X == c4X) { // Check If Same Num
								c5X = c4X * 2;
								c4X = 0;
								c2X = 0;
							} else {
								c5X = c4X;
								c4X = c2X;
								c2X = 0;
							}
						}

					} else {
						// "X", " ", " ", "X", " "
						if (c1X != 0) {

							if (c1X == c4X) { // Check If Same Num
								c5X = c4X * 2;
								c4X = 0;
								c1X = 0;
							} else {
								c5X = c4X;
								c4X = c1X;
								c1X = 0;
							}

						// " ", " ", " ", "X", " "
						} else {
							c5X = c4X;
							c4X = 0;
						}
					}
				}
			}

		// -- 3 --
		} else if (c3X != 0) {
			
			if (c5X != 0) {

				if (c2X != 0) {

					// "X", "X", "X", " ", "X"
					if (c1X != 0) {

						if (c3X == c5X) { // Check If Same Num
							if (c1X == c2X) { // Check If Same Num
								c5X = c5X * 2;
								c4X = c2X * 2;
								c3X = 0;
								c2X = 0;
								c1X = 0;
							} else {
								c5X = c5X * 2;
								c4X = c2X;
								c3X = c1X;
								c2X = 0;
								c1X = 0;
							}
						} else if (c3X == c2X) { // Check If Same Num
							// do nth for c5X
							c4X = c3X * 2;
							c3X = c1X;
							c2X = 0;
							c1X = 0;
						} else if (c1X == c2X) { // Check If Same Num
							// do nth for c5X
							c4X = c3X;
							c3X = c2X * 2;
							c2X = 0;
							c1X = 0;
						} else {
							// do nth for c5X
							c4X = c3X;
							c3X = c2X;
							c2X = c1X;
							c1X = 0;
						}

					// " ", "X", "X", " ", "X"
					} else {
						if (c3X == c5X) { // Check If Same Num
							c5X = c5X * 2;
							c4X = c2X;
							c3X = 0;
							c2X = 0;
						} else if (c3X == c2X) { // Check If Same Num
							// do nth for c5X
							c4X = c3X * 2;
							c3X = 0;
							c2X = 0;
						} else {
							// do nth for c5X
							c4X = c3X;
							c3X = c2X;
							c2X = 0;
						}
					}

				} else {
					// "X", " ", "X", " ", "X"
					if (c1X != 0) {

						if (c3X == c5X) { // Check If Same Num
							c5X = c5X * 2;
							c4X = c1X;
							c3X = 0;
							c1X = 0;
						} else if (c3X == c1X) { // Check If Same Num
							// do nth for c5X
							c4X = c3X * 2;
							c3X = 0;
							c1X = 0;
						} else {
							// do nth for c5X
							c4X = c3X
							c3X = c1X;
							c1X = 0;
						}

					// " ", " ", "X", " ", "X"
					} else {
						if (c3X == c5X) { // Check If Same Num
							c5X = c5X * 2;
							c3X = 0;
						} else {
							// do nth for c5X
							c4X = c3X
							c3X = 0;
						}
					}
				}

			} else {
				if (c2X != 0) {

					// "X", "X", "X", " ", " "
					if (c1X != 0) {

						if (c2X == c3X) { // Check If Same Num
							c5X = c3X * 2;
							c4X = c1X;
							c3X = 0;
							c2X = 0;
							c1X = 0;
						} else if (c2X == c1X) { // Check If Same Num
							c5X = c3X;
							c4X = c2X * 2;
							c3X = 0;
							c2X = 0;
							c1X = 0;
						} else {
							c5X = c3X;
							c4X = c2X;
							c3X = c1X;
							c2X = 0;
							c1X = 0;
						}

					// " ", "X", "X", " ", " "
					} else {
						if (c2X == c3X) { // Check If Same Num
							c5X = c3X * 2;
							c3X = 0;
							c2X = 0;
						} else {
							c5X = c3X;
							c4X = c2X;
							c3X = 0;
							c2X = 0;
						}
					}

				} else {
					// "X", " ", "X", " ", " "
					if (c1X != 0) {
					
						if (c1X == c3X) { // Check If Same Num
							c5X = c3X * 2;
							c3X = 0;
							c1X = 0;
						} else {
							c5X = c3X;
							c4X = c1X;
							c3X = 0;
							c1X = 0;
						}

					// " ", " ", "X", " ", " "
					} else {
						c5X = c3X;
						c3X = 0;
					}
				}
			}

		// -- 2 --
		} else if (c2X != 0) {
			
			if (c5X != 0) {

				// "X", "X", " ", " ", "X"
				if (c1X != 0) {

					if (c2X == c5X) { // Check If Same Num
						c5X = c5X * 2;
						c4X = c1X;
						c2X = 0;
						c1X = 0;
					} else if (c2X == c1X) { // Check If Same Num
						// do nth for c5X
						c4X = c2X * 2;
						c2X = 0;
						c1X = 0;
					} else {
						// do nth for c5X;
						c4X = c2X;
						c3X = c1X;
						c2X = 0;
						c1X = 0;
					}

				// " ", "X", " ", " ", "X"
				} else {
					if (c2X == c5X) { // Check If Same Num
						c5X = c5X * 2;
						c2X = 0;
					} else {
						// do nth for c5X
						c4X = c2X;
						c2X = 0;
					}
				}

			} else {
				// "X", "X", " ", " ", " "
				if (c1X != 0) {

					if (c1X == c2X) { // Check If Same Num
						c5X = c2X * 2;
						c2X = 0;
						c1X = 0;
					} else {
						c5X = c2X;
						c4X = c1X;
						c2X = 0;
						c1X = 0;
					}

				// " ", "X", " ", " ", " "
				} else {
					c5X = c2X;
					c2X = 0;
				}
			}

		// -- 1 --
		} else if (c1X != 0) {

			// "X", " ", " ", " ", "X"
			if (c5X != 0) {
				
				if (c1X == c5X) { // Check If Same Num
					c5X = c5X * 2;
					c1X = 0;
				} else {
					// do nth for c5X
					c4X = c1X;
					c1X = 0;
				}

			// "X", " ", " ", " ", " "
			} else {
				c5X = c1X;
				c1X = 0;
			}

		} else {
			// do nth
		}

		logGrid[("c1" + iStr)] = c1X;
		logGrid[("c2" + iStr)] = c2X;
		logGrid[("c3" + iStr)] = c3X;
		logGrid[("c4" + iStr)] = c4X;
		logGrid[("c5" + iStr)] = c5X;
	}
} // function goDown()


function goLeft() {
	// from column #5 to #1
	// Similar to goUp()

	for (let i = 1; i < 6; i++) { // for row #1 to #5
		let iStr = i.toString()

		let c1X = logGrid[("c" + iStr + "1")];
		let c2X = logGrid[("c" + iStr + "2")];
		let c3X = logGrid[("c" + iStr + "3")];
		let c4X = logGrid[("c" + iStr + "4")];
		let c5X = logGrid[("c" + iStr + "5")];

		// -- 2 --
		if (c2X != 0) {

			if (c1X != 0) {

				if (c3X != 0) {

					if (c4X != 0) {

						// "X", "X", "X", "X", "X"
						if (c5X != 0) {

							if (c1X == c2X) { // Check If Same Num
								if (c3X == c4X) { // Check If Same Num
									c1X = c1X * 2;
									c2X = c3X * 2;
									c3X = c5X;
									c4X = 0;
									c5X = 0;
								} else if (c4X == c5X) { // Check If Same Num
									c1X = c1X * 2;
									c2X = c3X;
									c3X = c4X * 2;
									c4X = 0;
									c5X = 0;
								}
								else {
									c1X = c1X * 2;
									c2X = c3X;
									c3X = c4X;
									c4X = c5X;
									c5X = 0;
								}
							} else if (c2X == c3X) { // Check If Same Num
								if (c4X == c5X) { // Check If Same Num
									// do nth for c1X
									c2X = c2X * 2;
									c3X = c4X * 2;
									c4X = 0;
									c5X = 0;
								} else {
									// do nth for c1X
									c2X = c2X * 2;
									c3X = c4X;
									c4X = c5X;
									c5X = 0;
								}
							} else if (c3X == c4X) { // Check If Same Num
								// do nth for c1X & c2X
								c3X = c3X * 2;
								c4X = c5X;
								c5X = 0;
							} else if (c4X == c5X) { // Check If Same Num
								// do nth for c1X, c2X & c3X
								c4X = c4X * 2;
								c5X = 0;
							} else {
								// do nth
							}

						// "X", "X", "X", "X", " "
						} else {
							if (c1X == c2X) { // Check If Same Num
								if (c3X == c4X) { // Check If Same Num
									c1X = c1X * 2;
									c2X = c3X * 2;
									c3X = 0;
									c4X = 0;
								} else {
									c1X = c1X * 2;
									c2X = c3X;
									c3X = c4X;
									c4X = 0;
								}
							} else if (c2X == c3X) { // Check If Same Num
								// do nth for c1X
								c2X = c2X * 2;
								c3X = c4X;
								c4X = 0;
							} else if (c3X == c4X) { // Check If Same Num
								// do nth for c1X & c2X
								c3X = c3X * 2;
								c4X = 0;
							} else {
								// do nth
							}	
						}

					} else {
						// "X", "X", "X", " ", "X"
						if (c5X != 0) {

							if (c1X == c2X) { // Check If Same Num
								if (c3X == c5X) { // Check If Same Num
									c1X = c1X * 2;
									c2X = c3X * 2;
									c3X = 0;
									c5X = 0;
								} else {
									c1X = c1X * 2;
									c2X = c3X;
									c3X = c5X;
									c5X = 0;
								}
							} else if (c2X == c3X) { // Check If Same Num
								// do nth for c1X
								c2X = c2X * 2;
								c3X = c5X;
								c5X = 0;
							} else if (c3X == c5X) { // Check If Same Num
								// do nth for c1X & c2X
								c3X = c3X * 2;
								c5X = 0;
							} else {
								// do nth for c1X, c2X & c3X
								c4X = c5X;
								c5X = 0;
							}

						// "X", "X", "X", " ", " "
						} else {
							if (c1X == c2X) { // Check If Same Num
								c1X = c1X * 2;
								c2X = c3X;
								c3X = 0;
							} else if (c2X == c3X) { // Check If Same Num
								// do nth for c1X
								c2X = c2X * 2;
								c3X = 0;
							} else {
								// do nth
							}
						}
					}

				} else {
					if (c4X != 0) {

						// "X", "X", " ", "X", "X"
						if (c5X != 0) {
							
							if (c1X == c2X) { // Check If Same Num
								if (c4X == c5X) { // Check If Same Num
									c1X = c1X * 2;
									c2X = c4X * 2;
									c4X = 0;
									c5X = 0;
								} else {
									c1X = c1X * 2;
									c2X = c4X;
									c3X = c5X;
									c4X = 0;
									c5X = 0;
								}
							} else if (c2X == c4X) { // Check If Same Num
								// do nth for c1X
								c2X = c2X * 2;
								c3X = c5X;
								c4X = 0;
								c5X = 0;
							} else if (c4X == c5X) { // Check If Same Num
								// do nth for c1X & c2X
								c3X = c4X * 2;
								c4X = 0;
								c5X = 0;
							} else {
								// do nth for c1X & c2X
								c3X = c4X;
								c4X = c5X;
								c5X = 0;
							}

						// "X", "X", " ", "X", " "
						} else {
							if (c1X == c2X) { // Check If Same Num
								c1X = c1X * 2;
								c2X = c4X;
								c4X = 0;
							} else if (c2X == c4X) { // Check If Same Num
								// do nth for c1X
								c2X = c2X * 2;
								c4X = 0;
							}
							else {
								// do nth for c1X & c2X
								c3X = c4X;
								c4X = 0;
							}	
						}

					} else { 
						// "X", "X", " ", " ", "X"
						if (c5X != 0) {

							if (c1X == c2X) { // Check If Same Num
								c1X = c1X * 2;
								c2X = c5X;
								c5X = 0;
							} else if (c2X == c5X) { // Check If Same Num
								// do nth for c1X
								c2X = c2X * 2;
								c5X = 0;
							} else {
								// do nth for c1X & c2X
								c3X = c5X;
								c5X = 0;
							}

						// "X", "X", " ", " ", " "
						} else {
							if (c1X == c2X) { // Check If Same Num
								c1X = c1X * 2;
								c2X = 0;
							} else {
								// do nth
							}
						}
					}
				}

			} else {
				if (c3X != 0) {

					if (c4X != 0) {

						// " ", "X", "X", "X", "X"
						if (c5X != 0) {

							if (c2X == c3X) { // Check If Same Num
								if (c4X == c5X) { // Check If Same Num
									c1X = c2X * 2;
									c2X = c4X * 2;
									c3X = 0;
									c4X = 0;
									c5X = 0;
								} else {
									c1X = c2X * 2;
									c2X = c4X;
									c3X = c5X;
									c4X = 0;
									c5X = 0;
								}
							} else if (c3X == c4X) { // Check If Same Num
								c1X = c2X;
								c2X = c3X * 2;
								c3X = c5X;
								c4X = 0;
								c5X = 0;
							} else if (c4X == c5X) { // Check If Same Num
								c1X = c2X;
								c2X = c3X;
								c3X = c4X * 2;
								c4X = 0;
								c5X = 0;
							} else {
								c1X = c2X;
								c2X = c3X;
								c3X = c4X;
								c4X = c5X;
								c5X = 0;
							}

						// " ", "X", "X", "X", " "
						} else {
							if (c2X == c3X) { // Check If Same Num
								c1X = c2X * 2;
								c2X = c4X;
								c3X = 0;
								c4X = 0;
							} else if (c3X == c4X) { // Check If Same Num
								c1X = c2X;
								c2X = c3X * 2;
								c3X = 0;
								c4X = 0;
							} else {
								c1X = c2X;
								c2X = c3X;
								c3X = c4X;
								c4X = 0;
							}
						}

					} else {
						// " ", "X", "X", " ", "X"
						if (c5X != 0) {

							if (c2X == c3X) { // Check If Same Num
								c1X = c2X * 2;
								c2X = c5X;
								c3X = 0;
								c5X = 0;
							} else if (c3X == c5X) { // Check If Same Num
								c1X = c2X;
								c2X = c3X * 2;
								c3X = 0;
								c5X = 0;
							} else {
								c1X = c2X;
								c2X = c3X;
								c3X = c5X;
								c5X = 0;
							}

						// " ", "X", "X", " ", " "
						} else {
							if (c2X == c3X) { // Check If Same Num
								c1X = c2X * 2;
								c2X = 0;
								c3X = 0;
							} else {
								c1X = c2X;
								c2X = c3X;
								c3X = 0;
							}
						}
					}

				} else {
					if (c4X != 0) {

						// " ", "X", " ", "X", "X"
						if (c5X != 0) {

							if (c2X == c4X) { // Check If Same Num
								c1X = c2X * 2;
								c2X = c5X;
								c4X = 0;
								c5X = 0;
							} else if (c4X == c5X) { // Check If Same Num
								c1X = c2X;
								c2X = c4X * 2;
								c4X = 0;
								c5X = 0;
							} else {
								c1X = c2X;
								c2X = c4X;
								c3X = c5X;
								c4X = 0;
								c5X = 0;
							}

						// " ", "X", " ", "X", " "
						} else {
							if (c2X == c4X) { // Check If Same Num
								c1X = c2X * 2;
								c2X = 0;
								c4X = 0;
							} else {
								c1X = c2X;
								c2X = c4X;
								c4X = 0;
							}
						}

					} else {
						// " ", "X", " ", " ", "X"
						if (c5X != 0) {

							if (c2X == c5X) { // Check If Same Num
								c1X = c2X * 2;
								c2X = 0;
								c5X = 0;
							} else {
								c1X = c2X;
								c2X = c5X;
								c5X = 0;
							}	

						// " ", "X", " ", " ", " "
						} else {
							c1X = c2X;
							c2X = 0;
						}
					}
				}
			}

		// -- 3 --
		} else if (c3X != 0) {

			if (c1X != 0) {

				if (c4X != 0) {

					// "X", " ", "X", "X", "X"
					if (c5X != 0) {

						if (c1X == c3X) { // Check If Same Num
							if (c4X == c5X) { // Check If Same Num
								c1X = c1X * 2;
								c2X = c4X * 2;
								c3X = 0;
								c4X = 0;
								c5X = 0;
							} else {
								c1X = c1X * 2;
								c2X = c4X;
								c3X = c5X;
								c4X = 0;
								c5X = 0;
							}
						} else if (c3X == c4X) { // Check If Same Num
							// do nth for c1X
							c2X = c3X * 2;
							c3X = c5X;
							c4X = 0;
							c5X = 0;
						} else if (c4X == c5X) { // Check If Same Num
							// do nth for c1X
							c2X = c3X;
							c3X = c4X * 2;
							c4X = 0;
							c5X = 0;
						} else {
							// do nth for c1X
							c2X = c3X;
							c3X = c4X;
							c4X = c5X;
							c5X = 0;
						}

					// "X", " ", "X", "X", " "
					} else {
						if (c1X == c3X) { // Check If Same Num
							c1X = c1X * 2;
							c2X = c4X;
							c3X = 0;
							c4X = 0;
						} else if (c3X == c4X) { // Check If Same Num
							// do nth for c1X
							c2X = c3X * 2;
							c3X = 0;
							c4X = 0;
						} else {
							// do nth for c1X
							c2X = c3X;
							c3X = c4X;
							c4X = 0;
						}	
					}

				} else {
					// "X", " ", "X", " ", "X"
					if (c5X != 0) {

						if (c1X == c3X) { // Check If Same Num
							c1X = c1X * 2;
							c2X = c5X;
							c3X = 0;
							c5X = 0;
						} else if (c3X == c5X) { // Check If Same Num
							// do nth for c1X
							c2X = c3X * 2;
							c3X = 0;
							c5X = 0;
						} else {
							// do nth for c1X
							c2X = c3X;
							c3X = c5X;
							c5X = 0;
						}

					// "X", " ", "X", " ", " "
					} else {
						if (c1X == c3X) { // Check If Same Num
							c1X = c1X * 2;
							c3X = 0;
						} else {
							// do nth for c1X
							c2X = c3X;
							c3X = 0;
						}
					}
				}

			} else {
				if (c4X != 0) {

					// " ", " ", "X", "X", "X"
					if (c5X != 0) {

						if (c3X == c4X) { // Check If Same Num
							c1X = c3X * 2;
							c2X = c5X;
							c3X = 0;
							c4X = 0;
							c5X = 0;
						} else if (c4X == c5X) { // Check If Same Num
							c1X = c3X;
							c2X = c4X * 2;
							c3X = 0;
							c4X = 0;
							c5X = 0;
						} else {
							c1X = c3X;
							c2X = c4X;
							c3X = c5X;
							c4X = 0;
							c5X = 0;
						}
					
					// " ", " ", "X", "X", " "
					} else {
						if (c3X == c4X) { // Check If Same Num
							c1X = c3X * 2;
							c3X = 0;
							c4X = 0;
						} else {
							c1X = c3X;
							c2X = c4X;
							c3X = 0;
							c4X = 0;
						}
					}
					
				} else {
					// " ", " ", "X", " ", "X"
					if (c5X != 0) {

						if (c3X == c5X) { // Check If Same Num
							c1X = c3X * 2;
							c3X = 0;
							c5X = 0;
						} else {
							c1X = c3X;
							c2X = c5X;
							c3X = 0;
							c5X = 0;
						}

					// " ", " ", "X", " ", " "
					} else {
						c1X = c3X;
						c3X = 0;
					}
				}
			}

		// -- 4 --
		} else if (c4X != 0) {

			if (c1X != 0) {

				// "X", " ", " ", "X", "X"
				if (c5X != 0) {

					if (c1X == c4X) { // Check If Same Num
						c1X = c1X * 2;
						c2X = c5X;
						c4X = 0;
						c5X = 0;
					} else if (c4X == c5X) { // Check If Same Num
						// do nth for c1X
						c2X = c4X * 2;
						c4X = 0;
						c5X = 0;
					} else {
						// do nth for c1X
						c2X = c4X;
						c3X = c5X;
						c4X = 0;
						c5X = 0;
					}

				// "X", " ", " ", "X", " "
				} else {
					if (c1X == c4X) { // Check If Same Num
						c1X = c1X * 2;
						c4X = 0;
					} else {
						// do nth for c1X
						c2X = c4X;
						c4X = 0;
					}
				}

			} else {
				// " ", " ", " ", "X", "X"
				if (c5X != 0) {

					if (c4X == c5X) { // Check If Same Num
						c1X = c4X * 2;
						c4X = 0;
						c5X = 0;
					} else {
						c1X = c4X;
						c2X = c5X;
						c4X = 0;
						c5X = 0;
					}

				// " ", " ", " ", "X", " "
				} else {
					c1X = c4X;
					c4X = 0;
				}
			}

		// -- 5 --
		} else if (c5X != 0) {

			// "X", " ", " ", " ", "X"
			if (c1X != 0) {

				if (c1X == c5X) { // Check If Same Num
					c1X = c1X * 2;
					c5X = 0;
				} else {
					// do nth for c1X
					c2X = c5X;
					c5X = 0;
				}

			// " ", " ", " ", " ", "X"
			} else {
				c1X = c5X;
				c5X = 0;
			}

		} else {
			// do nth
		}

		logGrid[("c" + iStr + "1")] = c1X;
		logGrid[("c" + iStr + "2")] = c2X;
		logGrid[("c" + iStr + "3")] = c3X;
		logGrid[("c" + iStr + "4")] = c4X;
		logGrid[("c" + iStr + "5")] = c5X;
	}
} // function goLeft()


function goRight() {
	// from column #1 to #5
	// Similar to goDown()

	for (let i = 1; i < 6; i++) { // for row #1 to #5
		let iStr = i.toString()

		let c1X = logGrid[("c" + iStr + "1")];
		let c2X = logGrid[("c" + iStr + "2")];
		let c3X = logGrid[("c" + iStr + "3")];
		let c4X = logGrid[("c" + iStr + "4")];
		let c5X = logGrid[("c" + iStr + "5")];

		// -- 4 --
		if (c4X != 0) {
			
			if (c5X != 0) {

				if (c3X != 0) {

					if (c2X != 0) {

						// "X", "X", "X", "X", "X"
						if (c1X != 0) {

							if (c5X == c4X) { // Check If Same Num
								if (c3X == c2X) { // Check If Same Num
									c5X = c5X * 2;
									c4X = c3X * 2;
									c3X = c1X;
									c2X = 0;
									c1X = 0;
								} else if (c2X == c1X) { // Check If Same Num
									c5X = c5X * 2;
									c4X = c3X;
									c3X = c2X * 2;
									c2X = 0;
									c1X = 0;
								} else {
									c5X = c5X * 2;
									c4X = c3X;
									c3X = c2X;
									c2X = c1X;
									c1X = 0;
								}
							} else if (c4X == c3X) { // Check If Same Num
								if (c2X == c1X) { // Check If Same Num
									// do nth for c5X
									c4X = c4X * 2;
									c3X = c2X * 2;
									c2X = 0;
									c1X = 0;
								} else {
									// do nth for c5X
									c4X = c4X * 2;
									c3X = c2X;
									c2X = c1X;
									c1X = 0;
								}
							} else if (c3X == c2X) { // Check If Same Num
								// do nth for c5X & c4X
								c3X = c3X * 2;
								c2X = c1X;
								c1X = 0;
							} else if (c2X == c1X) { // Check If Same Num
								// do nth for c5X, c4X & c3X
								c2X = c2X * 2;
								c1X = 0;
							} else {
								// do nth
							}

						// " ", "X", "X", "X", "X"
						} else {
							if (c5X == c4X) { // Check If Same Num
								if (c3X == c2X) { // Check If Same Num
									c5X = c5X * 2;
									c4X = c3X * 2;
									c3X = 0;
									c2X = 0;
								} else {
									c5X = c5X * 2;
									c4X = c3X;
									c3X = c2X;
									c2X = 0;
								}
							} else if (c4X == c3X) { // Check If Same Num
								// do nth for c5X
								c4X = c4X * 2;
								c3X = c2X;
								c2X = 0;
							} else if (c3X == c2X) { // Check If Same Num
								// do nth for c5X & c4X
								c3X = c3X * 2;
								c2X = 0;
							} else {
								// do nth
							}
						}

					} else {
						// "X", " ", "X", "X", "X"
						if (c1X != 0) {

							if (c5X == c4X) { // Check If Same Num
								if (c3X == c1X) { // Check If Same Num
									c5X = c5X * 2;
									c4X = c3X * 2;
									c3X = 0;
									c1X = 0;
								} else {
									c5X = c5X * 2;
									c4X = c3X;
									c3X = c1X;
									c1X = 0;
								}
							} else if (c3X == c4X) { // Check If Same Num
								// do nth for c5X
								c4X = c4X * 2;
								c3X = c1X;
								c1X = 0;
							} else if (c3X == c1X) { // Check If Same Num
								// do nth for c5X & c4X
								c3X = c3X * 2;
								c1X = 0;
							} else {
								// do nth for c5X, c4X & c3X
								c2X = c1X;
								c1X = 0;
							}

						// " ", " ", "X", "X", "X"
						} else {
							if (c5X == c4X) { // Check If Same Num
								c5X = c5X * 2;
								c4X = c3X;
								c3X = 0;
							} else if (c3X == c4X) { // Check If Same Num
								// do nth for c5X
								c4X = c4X * 2;
								c3X = 0;
							} else {
								// do nth
							}
						}
					}

				} else {
					if (c2X != 0) {

						// "X", "X", " ", "X", "X"
						if (c1X != 0) {

							if (c5X == c4X) { // Check If Same Num
								if (c2X == c1X) { // Check If Same Num
									c5X = c5X * 2;
									c4X = c2X * 2;
									c2X = 0;
									c1X = 0;
								} else {
									c5X = c5X * 2;
									c4X = c2X;
									c3X = c1X;
									c2X = 0;
									c1X = 0;
								}
							} else if (c2X == c4X) { // Check If Same Num
								// do nth for c5X
								c4X = c4X * 2;
								c3X = c1X;
								c2X = 0;
								c1X = 0;
							} else if (c2X == c1X) { // Check If Same Num
								// do nth for c5X & c4X
								c3X = c2X * 2;
								c2X = 0;
								c1X = 0;
							} else {
								// do nth for c5X & c4X
								c3X = c2X;
								c2X = c1X;
								c1X = 0;
							}

						// " ", "X", " ", "X", "X"
						} else {
							if (c5X == c4X) { // Check If Same Num
								c5X = c5X * 2;
								c4X = c2X;
								c2X = 0;
							} else if (c2X == c4X) { // Check If Same Num
								// do nth for c5X
								c4X = c4X * 2;
								c2X = 0;
							} else {
								// do nth for c5X & c4X
								c3X = c2X;
								c2X = 0;
							}
						}

					} else {
						// "X", " ", " ", "X", "X"
						if (c1X != 0) {

							if (c5X == c4X) { // Check If Same Num
								c5X = c5X * 2;
								c4X = c1X;
								c1X = 0;
							} else if (c1X == c4X) { // Check If Same Num
								// do nth for c5X
								c4X = c4X * 2;
								c1X = 0;
							} else {
								// do nth for c4X & c5X
								c3X = c1X;
								c1X = 0;
							}

						// " ", " ", " ", "X", "X"
						} else {
							if (c5X == c4X) { // Check If Same Num
								c5X = c5X * 2;
								c4X = 0;
							} else {
								// do nth
							}
						}
					}
				}

			} else {
				if (c3X != 0) {

					if (c2X != 0) {

						// "X", "X", "X", "X", " "
						if (c1X != 0) {

							if (c3X == c4X) { // Check If Same Num
								if (c2X == c1X) { // Check If Same Num
									c5X = c4X * 2;
									c4X = c2X * 2;
									c3X = 0;
									c2X = 0;
									c1X = 0;
								} else {
									c5X = c4X * 2;
									c4X = c2X;
									c3X = c1X;
									c2X = 0;
									c1X = 0;
								}
							} else if (c3X == c2X) { // Check If Same Num
								c5X = c4X;
								c4X = c3X * 2;
								c3X = c1X;
								c2X = 0;
								c1X = 0;
							} else if (c2X == c1X) { // Check If Same Num
								c5X = c4X;
								c4X = c3X;
								c3X = c2X * 2;
								c2X = 0;
								c1X = 0;
							} else {
								c5X = c4X;
								c4X = c3X;
								c3X = c2X;
								c2X = c1X;
								c1X = 0;
							}

						// " ", "X", "X", "X", " "
						} else {
							if (c3X == c4X) { // Check If Same Num
								c5X = c4X * 2;
								c4X = c2X;
								c3X = 0;
								c2X = 0;
							} else if (c3X == c2X) { // Check If Same Num
								c5X = c4X;
								c4X = c3X * 2;
								c3X = 0;
								c2X = 0;
							} else {
								c5X = c4X;
								c4X = c3X;
								c3X = c2X;
								c2X = 0;
							}
						}

					} else {
						// "X", " ", "X", "X", " "
						if (c1X != 0) {

							if (c3X == c4X) { // Check If Same Num
								c5X = c4X * 2;
								c4X = c1X;
								c3X = 0;
								c1X = 0;
							} else if (c1X == c3X) { // Check If Same Num
								c5X = c4X;
								c4X = c3X * 2;
								c3X = 0;
								c1X = 0;
							} else {
								c5X = c4X;
								c4X = c3X;
								c3X = c1X;
								c1X = 0;							}

						// " ", " ", "X", "X", " "
						} else {
							if (c3X == c4X) { // Check If Same Num
								c5X = c4X * 2;
								c4X = 0;
								c3X = 0;
							} else {
								c5X = c4X;
								c4X = c3X;
								c3X = 0;
							}
						}
					}

				} else {
					if (c2X != 0) {

						// "X", "X", " ", "X", " "
						if (c1X != 0) {

							if (c2X == c4X) { // Check If Same Num
								c5X = c4X * 2;
								c4X = c1X;
								c2X = 0;
								c1X = 0;
							} else if (c2X == c1X) { // Check If Same Num
								c5X = c4X;
								c4X = c2X * 2;
								c2X = 0;
								c1X = 0;
							} else {
								c5X = c4X;
								c4X = c2X;
								c3X = c1X;
								c2X = 0;
								c1X = 0;
							}

						// " ", "X", " ", "X", " "
						} else {
							if (c2X == c4X) { // Check If Same Num
								c5X = c4X * 2;
								c4X = 0;
								c2X = 0;
							} else {
								c5X = c4X;
								c4X = c2X;
								c2X = 0;
							}
						}

					} else {
						// "X", " ", " ", "X", " "
						if (c1X != 0) {

							if (c1X == c4X) { // Check If Same Num
								c5X = c4X * 2;
								c4X = 0;
								c1X = 0;
							} else {
								c5X = c4X;
								c4X = c1X;
								c1X = 0;
							}

						// " ", " ", " ", "X", " "
						} else {
							c5X = c4X;
							c4X = 0;
						}
					}
				}
			}

		// -- 3 --
		} else if (c3X != 0) {
			
			if (c5X != 0) {

				if (c2X != 0) {

					// "X", "X", "X", " ", "X"
					if (c1X != 0) {

						if (c3X == c5X) { // Check If Same Num
							if (c1X == c2X) { // Check If Same Num
								c5X = c5X * 2;
								c4X = c2X * 2;
								c3X = 0;
								c2X = 0;
								c1X = 0;
							} else {
								c5X = c5X * 2;
								c4X = c2X;
								c3X = c1X;
								c2X = 0;
								c1X = 0;
							}
						} else if (c3X == c2X) { // Check If Same Num
							// do nth for c5X
							c4X = c3X * 2;
							c3X = c1X;
							c2X = 0;
							c1X = 0;
						} else if (c1X == c2X) { // Check If Same Num
							// do nth for c5X
							c4X = c3X;
							c3X = c2X * 2;
							c2X = 0;
							c1X = 0;
						} else {
							// do nth for c5X
							c4X = c3X;
							c3X = c2X;
							c2X = c1X;
							c1X = 0;
						}

					// " ", "X", "X", " ", "X"
					} else {
						if (c3X == c5X) { // Check If Same Num
							c5X = c5X * 2;
							c4X = c2X;
							c3X = 0;
							c2X = 0;
						} else if (c3X == c2X) { // Check If Same Num
							// do nth for c5X
							c4X = c3X * 2;
							c3X = 0;
							c2X = 0;
						} else {
							// do nth for c5X
							c4X = c3X;
							c3X = c2X;
							c2X = 0;
						}
					}

				} else {
					// "X", " ", "X", " ", "X"
					if (c1X != 0) {

						if (c3X == c5X) { // Check If Same Num
							c5X = c5X * 2;
							c4X = c1X;
							c3X = 0;
							c1X = 0;
						} else if (c3X == c1X) { // Check If Same Num
							// do nth for c5X
							c4X = c3X * 2;
							c3X = 0;
							c1X = 0;
						} else {
							// do nth for c5X
							c4X = c3X
							c3X = c1X;
							c1X = 0;
						}

					// " ", " ", "X", " ", "X"
					} else {
						if (c3X == c5X) { // Check If Same Num
							c5X = c5X * 2;
							c3X = 0;
						} else {
							// do nth for c5X
							c4X = c3X
							c3X = 0;
						}
					}
				}

			} else {
				if (c2X != 0) {

					// "X", "X", "X", " ", " "
					if (c1X != 0) {

						if (c2X == c3X) { // Check If Same Num
							c5X = c3X * 2;
							c4X = c1X;
							c3X = 0;
							c2X = 0;
							c1X = 0;
						} else if (c2X == c1X) { // Check If Same Num
							c5X = c3X;
							c4X = c2X * 2;
							c3X = 0;
							c2X = 0;
							c1X = 0;
						} else {
							c5X = c3X;
							c4X = c2X;
							c3X = c1X;
							c2X = 0;
							c1X = 0;
						}

					// " ", "X", "X", " ", " "
					} else {
						if (c2X == c3X) { // Check If Same Num
							c5X = c3X * 2;
							c3X = 0;
							c2X = 0;
						} else {
							c5X = c3X;
							c4X = c2X;
							c3X = 0;
							c2X = 0;
						}
					}

				} else {
					// "X", " ", "X", " ", " "
					if (c1X != 0) {
					
						if (c1X == c3X) { // Check If Same Num
							c5X = c3X * 2;
							c3X = 0;
							c1X = 0;
						} else {
							c5X = c3X;
							c4X = c1X;
							c3X = 0;
							c1X = 0;
						}

					// " ", " ", "X", " ", " "
					} else {
						c5X = c3X;
						c3X = 0;
					}
				}
			}

		// -- 2 --
		} else if (c2X != 0) {
			
			if (c5X != 0) {

				// "X", "X", " ", " ", "X"
				if (c1X != 0) {

					if (c2X == c5X) { // Check If Same Num
						c5X = c5X * 2;
						c4X = c1X;
						c2X = 0;
						c1X = 0;
					} else if (c2X == c1X) { // Check If Same Num
						// do nth for c5X
						c4X = c2X * 2;
						c2X = 0;
						c1X = 0;
					} else {
						// do nth for c5X;
						c4X = c2X;
						c3X = c1X;
						c2X = 0;
						c1X = 0;
					}

				// " ", "X", " ", " ", "X"
				} else {
					if (c2X == c5X) { // Check If Same Num
						c5X = c5X * 2;
						c2X = 0;
					} else {
						// do nth for c5X
						c4X = c2X;
						c2X = 0;
					}
				}

			} else {
				// "X", "X", " ", " ", " "
				if (c1X != 0) {

					if (c1X == c2X) { // Check If Same Num
						c5X = c2X * 2;
						c2X = 0;
						c1X = 0;
					} else {
						c5X = c2X;
						c4X = c1X;
						c2X = 0;
						c1X = 0;
					}

				// " ", "X", " ", " ", " "
				} else {
					c5X = c2X;
					c2X = 0;
				}
			}

		// -- 1 --
		} else if (c1X != 0) {

			// "X", " ", " ", " ", "X"
			if (c5X != 0) {
				
				if (c1X == c5X) { // Check If Same Num
					c5X = c5X * 2;
					c1X = 0;
				} else {
					// do nth for c5X
					c4X = c1X;
					c1X = 0;
				}

			// "X", " ", " ", " ", " "
			} else {
				c5X = c1X;
				c1X = 0;
			}

		} else {
			// do nth
		}

		logGrid[("c" + iStr + "1")] = c1X;
		logGrid[("c" + iStr + "2")] = c2X;
		logGrid[("c" + iStr + "3")] = c3X;
		logGrid[("c" + iStr + "4")] = c4X;
		logGrid[("c" + iStr + "5")] = c5X;
	}
} // function goRight()


function genNum() {
	let num = randNum();
	// Kary: randPos() can be further optimized
	let pos = randPos();

	while (logGrid[pos] != 0) {
		pos = randPos();
	}

	logGrid[pos] = num;

	printGrid(pos, num);
} // function genNum()


function reset() {
	logGrid = {
		"c11": 0, "c12": 0, "c13": 0, "c14": 0, "c15": 0,
		"c21": 0, "c22": 0, "c23": 0, "c24": 0, "c25": 0,
		"c31": 0, "c32": 0, "c33": 0, "c34": 0, "c35": 0,
		"c41": 0, "c42": 0, "c43": 0, "c44": 0, "c45": 0,
		"c51": 0, "c52": 0, "c53": 0, "c54": 0, "c55": 0
	};

	currentScore = 0;
} // function reset()


function randNum() {
	// Random function to generate either 2 or 4
	let num = Math.floor(Math.random() * 2);
	if (num == 0) {
		return 2;
	} else {
		return 4;
	}
} // function randNum()


function randPos() {
	let rowNum = Math.floor(Math.random() * 5) + 1;
	let colNum = Math.floor(Math.random() * 5) + 1;
	let pos = "c" + rowNum.toString() + colNum.toString();
	return pos;
} // function randPos()


function checkIfGameOver() {
	for (let gridCell in logGrid) {
		if (logGrid[gridCell] == 0) {
			return false;
		}
	}
	return true;
} // function checkIfGameOver()


function printGrid(pos, num) {
	currentScore = currentScore + num;

	// Kary
	// let checkScore = 0;

	for (let gridCell in logGrid) {
		if (logGrid[gridCell] == 0) {
			document.getElementById(gridCell).innerHTML = "";
			document.getElementById(gridCell).style.color = "#0ABAB5";
		} else {
			document.getElementById(gridCell).innerHTML = logGrid[gridCell].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
			document.getElementById(gridCell).style.color = "#0ABAB5";

			// Kary: Check Score
			// checkScore = checkScore + logGrid[gridCell];
		}
	}

	// Highlight newly generate num
	document.getElementById(pos).style.color = "#FF0000";

	// Update current score
	document.getElementById("currentScore").innerHTML = currentScore.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");

	// Kary
	// if (currentScore != checkScore) {
	// 	alert("stop");	
	// }
} // function printGrid()