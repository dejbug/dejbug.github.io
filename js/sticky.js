'use strict';

function Sticky()
{
	this.targets = null;
	this.lastNearestAbove = null;
	this.lastScrollTop = -1;

	this.findNearestItemAbove = function()
	{
		const targetsAbove = _.filter(this.targets,
			target => target.offsetTop < document.scrollingElement.scrollTop);
		return targetsAbove.length ? targetsAbove[targetsAbove.length - 1] : null;
	}

	this.update = function()
	{
		const scrollTop = document.scrollingElement.scrollTop;
		if (scrollTop == this.lastScrollTop) return;
		this.lastScrollTop = scrollTop;

		const nearestAbove = this.findNearestItemAbove();
		if (this.lastNearestAbove == nearestAbove) return;
		this.lastNearestAbove = nearestAbove;

		this.onchange(this.lastNearestAbove);
	}

	this.onchange = function(item) { }

	this.timerCallback = function(event)
	{
		this.update();
	}

	this.register = function(targets)
	{
		console.assert(this.targets === null);
		this.targets = targets;
		this.update();
		window.setInterval(this.timerCallback.bind(this), 100);
	}

	this.registerQuery = function(query)
	{
		this.register(document.querySelectorAll(query));
	}

	this.unregister = function()
	{
		console.assert(this.targets !== null);
		window.clearInterval(this.timerCallback);
		this.targets = null;
	}
}

const status = document.querySelector('#status');
const sticky = new Sticky();
sticky.registerQuery('h3');
sticky.onchange = function(item)
{
	const textContent = item ? item.textContent : null;
	status.textContent = textContent;
};
