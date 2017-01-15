(function(list)
{
	for (var k = list.length - 1; k >= 0; --k)
	{
		var element = list[k];

		switch (element.firstChild.nodeValue)
		{
			case "♥":
			case "♦":
				element.classList.add("redsuit");
		}
	}
})(document.getElementsByTagName("em"));
