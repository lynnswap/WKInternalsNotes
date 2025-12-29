# ``WKInternalsNotes/WKPDFPageNumberIndicator/updatePosition(_:)``

安全領域と被覆領域を考慮して表示位置を更新する。

## Objective-C Declaration
```objective-c
- (void)updatePosition:(CGRect)frame;
```

## Discussion
`WKWebView` の安全領域/被覆領域の inset を合算し、`frame` の原点を補正して移動する。移動後に `sizeToFit` と `show` を呼ぶ。

## References
- [`WKPDFPageNumberIndicator.mm#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFPageNumberIndicator.mm#L121)
- [`WKPDFPageNumberIndicator.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFPageNumberIndicator.h#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
