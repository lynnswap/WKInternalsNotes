# ``WKInternalsNotes/_WKTextRun/rectInWebView``

内部の `API::TextRun` が持つ WebView 座標の矩形を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGRect rectInWebView;
```

## Default Value
`API::TextRun` の矩形に依存。

## Discussion
`Ref { *_textRun }->rectInWebView()` をそのまま返す。

## References
- [`_WKTextRun.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextRun.h#L36)
- [`_WKTextRun.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextRun.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
