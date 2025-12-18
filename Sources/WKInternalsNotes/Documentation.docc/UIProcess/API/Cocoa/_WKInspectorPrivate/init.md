# ``WKInternalsNotes/_WKInspector/init()``

この初期化子は使用できない（`NS_UNAVAILABLE`）。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_UNAVAILABLE;
```

## Discussion
`init` はヘッダで `NS_UNAVAILABLE` として宣言されている。実体は `WKWebView` の `_inspector` アクセサ経由で取得されるため、直接生成しない。

## References
- [`_WKInspector.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L41)
- [`WKWebView.mm#L3791`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3791)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
