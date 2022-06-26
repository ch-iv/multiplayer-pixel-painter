<script>
	import io from 'socket.io-client';
	import { onMount } from 'svelte';
	import Two from 'two.js';
	
	var pixel_size = 20;
	var socket = io();
	var two;
	var color = [0,0,0];


    socket.on('connect', () => {
        socket.emit('connection_event');
    });

	socket.on("board_full", (board) => {
		draw_board(board.pixels, pixel_size);
	});

	socket.on("pixel_change", (pixel) => {
		draw_pixel(pixel.x, pixel.y, pixel.color, pixel_size);
	});

	onMount(async () => {
		var params = { fullscreen: true, autostart: true };
		var elem = document.body;
		two = new Two(params).appendTo(elem);

		onmousedown = function(event){
			let coords = mouse_coord_to_pixel_coord(event.clientX, event.clientY, pixel_size);
			socket.emit('set_pixel', {x: coords.x, y: coords.y, color: color});
		}
		
	});

	function mouse_coord_to_pixel_coord(x, y, pixel_size){
		return {x: Math.floor(x/pixel_size), y: Math.floor(y/pixel_size)};
	}

	function draw_board(pixels, pixel_size){
		for (let y = 0; y < pixels.length; y++) {
			for (let x = 0; x < pixels[y].length; x++){
				


				let y_coord = y * pixel_size + (pixel_size * 0.5);
				let x_coord = x * pixel_size + (pixel_size * 0.5);
				var rect = two.makeRectangle(x_coord, y_coord, pixel_size, pixel_size);

				rect.fill = color_to_string(pixels[y][x]);
				rect.opacity = 1;
				rect.stroke = 'rgb(0,0,0)';
			}
		} 
		two.update();
	}

	function draw_pixel(x, y, color, pixel_size){
		let y_coord = y * pixel_size + (pixel_size * 0.5);
		let x_coord = x * pixel_size + (pixel_size * 0.5);
		var rect = two.makeRectangle(x_coord, y_coord, pixel_size, pixel_size);

		rect.fill = color_to_string(color);
		rect.opacity = 1;
		rect.stroke = 'rgb(0,0,0)';
		two.update();
	}



	function color_to_string(color){
		// color is a list of 3 ints
		return 'rgb(' + color[0].toString() + ',' + color[1].toString() + ',' + color[2].toString() + ')';
	
	}


	document.addEventListener('keydown', (event) => {
		let key = event.key;
		switch (key){
			case "1":
				color = [153, 194, 77];
				break;
			case "2":
				color = [241, 143, 1];
				break;
			case "3":
				color = [4, 139, 168];
				break;
			case "4":
				color = [47, 45, 46];
				break;
			case "5":
				color = [250, 166, 255];
				break;
			case "6":
				color = [196, 69, 54];
				break;
		}
	}, false);

</script>