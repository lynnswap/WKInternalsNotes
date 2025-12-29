# ``WKInternalsNotes/_WKInspectorWindow/inspectedWebView``

関連付けられた `WKWebView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, readonly, weak) WKWebView *inspectedWebView WK_API_AVAILABLE(macos(13.3));
```

## Default Value
`nil`。

## Discussion
公開ヘッダでは読み取り専用、内部ヘッダでは `readwrite` の弱参照として宣言されており、特別な実装はなく自動合成で保持される。

## References
- [`_WKInspectorWindow.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorWindow.h#L38)
- [`_WKInspectorWindowInternal.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorWindowInternal.h#L35)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
