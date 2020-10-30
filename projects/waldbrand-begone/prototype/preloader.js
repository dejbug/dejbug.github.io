function preload(urls, index, onDone) {
	// [src: https://www.photo-mark.com/notes/image-preloading/]
	index = index || 0;
	if (urls && index < urls.length) {
		var img = new Image ();
		img.onload = function() {
			if (index + 1 < urls.length)
				preload(urls, index + 1, onDone);
			else
				onDone();
		}
		img.src = urls[index];
	}
}
