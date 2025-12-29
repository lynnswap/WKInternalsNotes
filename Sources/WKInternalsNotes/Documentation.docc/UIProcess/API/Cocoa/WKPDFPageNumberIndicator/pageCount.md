# ``WKInternalsNotes/WKPDFPageNumberIndicator/pageCount``

総ページ数を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) unsigned pageCount;
```

## Default Value
`0`。

## Discussion
`setPageCount:` は非 0 を要求し、変更があれば `_pageCount` を更新して `_updateLabel:` を呼ぶ。`_currentPageNumber` と揃ったときに表示更新される。

## References
- [`WKPDFPageNumberIndicator.mm#L145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFPageNumberIndicator.mm#L145)
- [`WKPDFPageNumberIndicator.mm#L220`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFPageNumberIndicator.mm#L220)
- [`WKPDFPageNumberIndicator.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFPageNumberIndicator.h#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
