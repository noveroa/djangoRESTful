//Python has a zip function (yaya!) but Java does not seem so simple
//Here I try to write a little function checking for longest given array and
//then pushing to a total flattened array
//
//set some test cases

var a = ['grapes', 'apples']
var b = ['foo', 'bar', 'etc, etc']
var c = ['milo']
var I = [a, b,c]


var zipp = function(arrays){
  // initialize an empty array to create the new flattened zipped one;
	var d = []
	//find the max length array;
	var maxl = 0
	for(var i =0;i <arrays.length; i++){
    	if (arrays[i].length >= maxl){
    		maxl = arrays[i].length
    	};
	};
  // now zip!
  for (var i =0; i< maxl; i++){
		for (var x =0; x< arrays.length; x++){
     	d.push(I[x][i])
      };
	};
  return d;
};

console.log('the end', zipp(I))