<!-- 
| Element Name | Dublin Core Mapping | Value Scheme | Obligation | Occurence | Input Guidelines | Examples |

| objectid      | Identifier  | | M|NR| objectid should be in the form `cbp_NNN`, where NNN is a sequential 3-digit zero-padded number           |    `cbp_001`<br/>`cbp_027`<br/>`cbp_239`      |
| parentid      | Relation | |MA|NR|            |          | 
| title         | Title       | | M| R|            |          |
| scope         |             | |  |  |            |          |
| note          |             | |  |  |            |          |
| description   | Description | | M|NR|            |          |
| creator       | Creator     | [LC Name Authority File](https://id.loc.gov/authorities/names.html) (LCNAF) |  | R|            |     <span style="white-space: nowrap;">`Kirby, Jack`</span><br/><span style="white-space: nowrap;">`Windsor-Smith, Barry`</span><br/>`Romita, John, Jr.`<br/>`Wolverton, Basil`     |
| date          | Date        | [W3C Date and Time Formats](https://www.w3.org/TR/NOTE-datetime)| MA |NR|   |            |
| paratext type | Subject   | |MA| R|            |            |
| tag           | Subject   | |MA| R|            |            |
| source        | Source    | |MA|NR|            |            |
| gcd id        | Relation  | |MA|NR| Find the specific issue at the Grand Comics Database at [comics.org](https://comics.org). The `gcd id` is the number following `https://www.comics.org/issue/` in the URL. For example, for _Fantastic Four_ #11, the URL to the issue is <https://www.comics.org/issue/17516/>, and the `gcd id` is `17516`.          |`99`<br/>`17516`<br/>`293`<br/>`601`            |
| type          | Type      | |MA|NR|            |            |
| format        | Format    | [IANA Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml) | M|NR|   | `image/jpeg`<br/>`image/png`<br/>`image/svg+xml` |  
|language       | Language  | [ISO 639-1 3-letter Language Codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) | M| R|        |  `eng`<br/>`fre`         |
| rights        | Rights    | |  |  |            |            |
| rightsstatement | Rights    | |  |  |            |            |


objectid	parentid	title	scope note	creator	date	description	paratext type	tag	source	gcd id	gcd link	type	format	language	rights	rightsstatement	display_template	object_location	image_small	image_thumb
-->

<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>

<thead>
<tr>
	<th>Element Name</th>
	<th>Dublin Core Mapping</th>
	<th>Value Scheme</th>
	<th>Obligation</th>
	<th>Occurence</th>
	<th>Input Guidelines</th>
	<th>Examples</th>
</tr>
</thead>

<tbody>
<tr>
	<td>objectid</td>
	<td>Identifier</td>
	<td></td>
	<td>M</td>
	<td>NR</td>
	<td>objectid should be in the form <code>cbp_NNN</code>, where NNN is a sequential 3-digit zero-padded number</td>
	<td>
		<ul style="list-style-type: '- ';">
			<li><code>cbp_001</code></li>
			<li><code>cbp_027</code></li>
			<li><code>cbp_239</code></li>
		</ul>	
	</td>
</tr>
<tr>
	<td>parentid</td>
	<td>Relation</td>
	<td></td>
	<td>MA</td>
	<td>NR</td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>title</td>
	<td>Title</td>
	<td></td>
	<td>M</td>
	<td>R</td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>scope</td>
	<td></td>
	<td></td>
	<td></td>
	<td></td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>note</td>
	<td></td>
	<td></td>
	<td></td>
	<td></td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>description</td>
	<td>Description</td>
	<td></td>
	<td>M</td>
	<td>NR</td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>creator</td>
	<td>Creator</td>
	<td><a href="https://id.loc.gov/authorities/names.html">LC Name Authority File</a> (LCNAF)</td>
	<td></td>
	<td>R</td>
	<td></td>
	<td>
		<ul style="list-style-type: '- ';">
			<li style="white-space: nowrap;"><code>Kirby, Jack</code></li>
			<li style="white-space: nowrap;"><code>Windsor-Smith, Barry</code>
			<li style="white-space: nowrap;"><code>Romita, John, Jr.</code></li>
			<li style="white-space: nowrap;"><code>Wolverton, Basil</code></li>
		</ul>
	</td>
</tr>
<tr>
	<td>date</td>
	<td>Date</td>
	<td><a href="https://www.w3.org/TR/NOTE-datetime">W3C Date and Time Formats</a></td>
	<td>MA</td>
	<td>NR</td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>paratext type</td>
	<td>Subject</td>
	<td></td>
	<td>MA</td>
	<td>R</td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>tag</td>
	<td>Subject</td>
	<td></td>
	<td>MA</td>
	<td>R</td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>source</td>
	<td>Source</td>
	<td></td>
	<td>MA</td>
	<td>NR</td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>gcd id</td>
	<td>Relation</td>
	<td></td>
	<td>MA</td>
	<td>NR</td>
	<td>Find the specific issue at the Grand Comics Database at <a href="https://comics.org">comics.org</a>. The <code>gcd id</code> is the number following <code>https://www.comics.org/issue/</code> in the URL. For example, for <em>Fantastic Four</em> #11, the URL to the issue is <a class="autolink" href="https://www.comics.org/issue/17516/">https://www.comics.org/issue/17516/</a>, and the <code>gcd id</code> is <code>17516</code>.</td>
	<td>
		<ul style="list-style-type: '- ';">
			<li><code>99</code></li>
			<li><code>17516</code></li>
			<li><code>293</code></li>
			<li><code>601</code></li>
		</ul>
	</td>
</tr>
<tr>
	<td>type</td>
	<td>Type</td>
	<td></td>
	<td>MA</td>
	<td>NR</td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>format</td>
	<td>Format</td>
	<td><a href="https://www.iana.org/assignments/media-types/media-types.xhtml">IANA Media Types</a></td>
	<td>M</td>
	<td>NR</td>
	<td></td>
	<td><ul style="list-style-type: '- ';">
		<li><code>image/jpeg</code></li><li><code>image/png</code></li><li><code>image/svg+xml</code></li></ul></td>
</tr>
<tr>
	<td>language</td>
	<td>Language</td>
	<td><a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">ISO 639-1 3-letter Language Codes</a></td>
	<td>M</td>
	<td>R</td>
	<td></td>
	<td><ul style="list-style-type: '- ';"><li><code>eng</code></li><li><code>fre</code></li></ul></td>
</tr>
<tr>
	<td>rights</td>
	<td>Rights</td>
	<td></td>
	<td></td>
	<td></td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>rightsstatement</td>
	<td>Rights</td>
	<td></td>
	<td></td>
	<td></td>
	<td></td>
	<td></td>
</tr>
</tbody>
</table>

**Legend**
<ul style="list-style-type: '- ';">
	<li><code>M</code>  Mandatory</li>
<li><code>MA</code> Mandatory, if applicable</li>
<li><code>R</code>  Repeatable</li>
<li><code>NR</code> Not repeatable</li>
</ul>