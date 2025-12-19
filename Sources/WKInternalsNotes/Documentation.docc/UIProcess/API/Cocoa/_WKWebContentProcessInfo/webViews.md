# ``WKInternalsNotes/_WKWebContentProcessInfo/webViews``

アクティブな WebContentProcess に紐づく `WKWebView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray<WKWebView *> *webViews;
```

## Discussion
`webContentState` がアクティブのときだけ `process.pages()` の `cocoaView()` を収集し、`webViews` で返す。prewarmed/cached では `_webViews` が作られないため `nil` を返す。

## References
- [`WKProcessPoolPrivate.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L66)
- [`WKProcessPool.mm#L807`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L807)
- [`WKProcessPool.mm#L827`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L827)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
