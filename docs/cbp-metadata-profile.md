| Element Name | Dublin Core Mapping | Value Scheme | Obligation | Occurence | Input Guidelines | Examples |
| ------------ | ------------------- | ------------ | ---------- | --------- | ---------------- | -------- |
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

**Legend**
- `M`  Mandatory
- `MA` Mandatory, if applicable
- `R`  Repeatable
- `NR` Not repeatable