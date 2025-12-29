# ``WKInternalsNotes/WKPDFPageNumberIndicator/currentPageNumber``

現在ページ番号を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) unsigned currentPageNumber;
```

## Default Value
`0`。

## Discussion
`setCurrentPageNumber:` は非 0 を要求し、変更があれば `_currentPageNumber` を更新して `_updateLabel:` を呼ぶ。`_pageCount` と `currentPageNumber` が揃ったときに表示更新される。

## References
- [`WKPDFPageNumberIndicator.mm#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFPageNumberIndicator.mm#L136)
- [`WKPDFPageNumberIndicator.mm#L220`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFPageNumberIndicator.mm#L220)
- [`WKPDFPageNumberIndicator.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFPageNumberIndicator.h#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
