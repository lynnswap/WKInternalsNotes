# ``WKInternalsNotes/WKPDFPageNumberIndicator/initWithFrame(_:view:pageCount:)``

ページ数表示インジケータを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(CGRect)frame view:(WKWebView *)view pageCount:(size_t)pageCount;
```

## Discussion
`WKWebView` を保持し、透明・非操作のビューとして初期化する。背景エフェクトとラベルを構築し、`updatePosition:` と `setPageCount:` を呼んで初期状態を整える。

## References
- [`WKPDFPageNumberIndicator.mm#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFPageNumberIndicator.mm#L62)
- [`WKPDFPageNumberIndicator.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFPageNumberIndicator.h#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
