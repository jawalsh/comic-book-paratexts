---
title: Metadata Profile for Comic Book Paratexts
layout: about
permalink: /metadata-profile.html
# include CollectionBuilder info at bottom
credits: true
---
{% include feature/jumbotron.html objectid="cbp_314" heading="About: Metadata Profile" text="The descriptive and bibliographic metadata for CBP." %} 

<div>
<h1>Metadata Profile for <cite>Comic Book Paratexts</cite></h1>
<div class="table-responsive">
<table class="table table-sm table-striped">

<thead>
<tr>
	<th><strong>Element Name</strong></th>
	<th><strong>Dublin Core Mapping</strong></th>
	<th><strong>Value Scheme</strong></th>
	<th><strong>Obligation</strong></th>
	<th><strong>Occurence</strong></th>
	<th><strong>Input Guidelines</strong></th>
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
	<td>objectid should be in the form cbp_NNN, where NNN is a sequential 3-digit zero-padded number</td>
	<td><ul><li><code>cbp_001</code></li><li><code>cbp_027</code></li><li><code>cbp_239</code></li></ul></td>
</tr>
<tr>
	<td>parentid</td>
	<td>Relation</td>
	<td></td>
	<td>MA</td>
	<td>NR</td>
	<td>Include for objects w/in a compound object. Should appear as the objectid of the compound object in which it is contained.</td>
	<td><ul><li><code>cbp_001</code></li></ul></td>
</tr>
<tr>
	<td>title</td>
	<td>Title</td>
	<td></td>
	<td>M</td>
	<td>R</td>
	<td>Combines ‘paratext type,’ ‘source,’ and scope fields. Title should appear in the form: [paratext type]: [source]. {Scope}</td>
	<td>
		<ul>
			<li><code>Correspondence: &quot;Let’s Level with Daredevil.” Daredevil #36 (January 1968). Marvel comics.</code></li>
			<li><code>Publisher’s peritext: Justice Society of America #4 (July 2023). DC Comics.</code></li>
			<li><code>Advertisement: “Honor House Products.” Dennis the Menace and His Friends Series #10 (June 1971). Fawcett Publications. Full page.</code></li>
		</ul>
	</td>
</tr>
<tr>
	<td>scope</td>
	<td></td>
	<td></td>
	<td>MA</td>
	<td>NR</td>
	<td>Include for objects w/in a compound object. Describe the extent of the image.</td>
	<td><ul><li><code>Full page</code></li><li><code>Detail</code></li></ul></td>
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
	<td>Briefly describe the object in question and what it contains.</td>
	<td><ul><li><code>“Bullseye is finally here,” advertisement for The Charlton Bullseye prozine with mail-in form for subscriptions to Charlton comics.</code></li><li><code>“Pin-up” illustration following main feature.</code></li></ul></td>
</tr>
<tr>
	<td>creator</td>
	<td>Creator</td>
	<td><a href="https://id.loc.gov/authorities/names.html">LC Name Authority File</a> (LCNAF)</td>
	<td>MA</td>
	<td>R</td>
	<td>Follow format provided on LCNAF. If multiple creators, separate by semicolons.</td>
	<td><ul><li><code>Kirby, Jack</code></li><li><code>Windsor-Smith, Barry</code></li><li><code>Romita, John, Jr.</code></li><li><code>Wolverton, Basil</code></li></ul></td>
</tr>
<tr>
	<td>date</td>
	<td>Date</td>
	<td><a href="https://www.w3.org/TR/NOTE-datetime">W3C Date and Time Formats</a></td>
	<td>MA</td>
	<td>NR</td>
	<td>[Year]-{[Month]}</td>
	<td><ul><li><code>1954-06</code></li><li><code>1963</code></li></ul></td>
</tr>
<tr>
	<td>paratext type</td>
	<td>Subject</td>
	<td></td>
	<td>MA</td>
	<td>R</td>
	<td>See metadata profile companion (forthcoming)</td>
	<td><ul><li><code>Correspondence</code></li><li><code>Advertisement</code></li></ul></td>
</tr>
<tr>
	<td>tag</td>
	<td>Subject</td>
	<td></td>
	<td>MA</td>
	<td>R</td>
	<td>See metadata profile companion (forthcoming)</td>
	<td><ul><li><code>gender</code></li><li><code>reader-contributed content</code></li></ul></td>
</tr>
<tr>
	<td>source</td>
	<td>Source</td>
	<td></td>
	<td>MA</td>
	<td>NR</td>
	<td>“[Paratext Heading/Title]” [Comic series] #[issue number] ([Full month] [Year]). [Publisher]</td>
	<td><ul><li><code>Animal Man #8 (February 1989). DC Comics.</code></li><li><code>Adventure Comics #485 (September 1981). DC Comics.</code></li></ul></td>
</tr>
<tr>
	<td>image_source</td>
	<td></td>
	<td></td>
	<td>MA</td>
	<td>NR</td>
	<td>[Website or repository of image]</td>
	<td><ul><li><code>Personal collection</code></li><li><code>Comic Book Plus</code></li><li><code>Digital Comic Museum</code></li><li><code>Internet Archive</code></li></ul></td>
</tr>
<tr>
	<td>image_source_link</td>
	<td></td>
	<td></td>
	<td>MA</td>
	<td>NR</td>
	<td>Include for images sourced from websites. [URL for page from which the source was retrieved]</td>
	<td><ul><li><a href="https://comicbookplus.com/?dlid=62348">https://comicbookplus.com/?dlid=62348</a></li><li><a href="https://digitalcomicmuseum.com/index.php?dlid=1014">https://digitalcomicmuseum.com/index.php?dlid=1014</a></li></ul></td>
</tr>
<tr>
	<td>gcd id</td>
	<td>Relation</td>
	<td></td>
	<td>MA</td>
	<td>NR</td>
	<td>Find the specific issue at the Grand Comics Database at <a href="http://comics.org">comics.org</a>. The gcd id is the number following <a href="https://www.comics.org/issue/">https://www.comics.org/issue/</a> in the URL. For example, for <em>Fantastic Four</em> #11, the URL to the issue is <a href="https://www.comics.org/issue/17516/">https://www.comics.org/issue/17516/</a>, and the gcd id is 17516.</td>
	<td><ul><li><code>99</code></li><li><code>17516</code></li><li><code>293</code></li><li><code>601</code></li></ul></td>
</tr>
<tr>
	<td>type</td>
	<td>Type</td>
	<td><a href="https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/2003-02-12/">DCMI Type Vocabulary</a></td>
	<td>MA</td>
	<td>NR</td>
	<td>Follow format on DCMI. If multiple, separate by semicolon. Usually just Image and StillImage.</td>
	<td><ul><li><code>Image;StillImage</code></li><li><code>Text</code></li></ul></td>
</tr>
<tr>
	<td>format</td>
	<td>Format</td>
	<td><a href="https://www.iana.org/assignments/media-types/media-types.xhtml">IANA Media Types</a></td>
	<td>M</td>
	<td>NR</td>
	<td>Follow format on IANA</td>
	<td><ul><li><code>image/jpeg</code></li><li><code>image/png</code></li><li><code>image/svg+xml</code></li></ul></td>
</tr>
<tr>
	<td>language</td>
	<td>Language</td>
	<td><a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">ISO 639-1 3-letter Language Codes</a></td>
	<td>M</td>
	<td>R</td>
	<td></td>
	<td><ul><li><code>eng</code></li><li><code>fre</code></li></ul></td>
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
	<td><a href="https://rightsstatements.org/page/1.0/?language=en">RightsStatements.org</a></td>
	<td></td>
	<td></td>
	<td></td>
	<td></td>
</tr>
</tbody>
</table>
</div>
<div>
<h2>Legend</h2>

<ul>
<li><code>M</code> Mandatory</li>
<li><code>MA</code> Mandatory, if applicable</li>
<li><code>R</code> Repeatable</li>
<li><code>NR</code> Not repeatable</li>
</ul>
</div>
</div>
