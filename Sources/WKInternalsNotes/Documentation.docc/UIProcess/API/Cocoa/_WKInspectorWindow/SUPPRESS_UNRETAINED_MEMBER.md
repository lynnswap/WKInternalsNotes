# ``WKInternalsNotes/_WKInspectorWindow/SUPPRESS_UNRETAINED_MEMBER``

`inspectedWebView` の弱参照宣言に付与された内部向けマクロ。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, readwrite, weak) WKWebView *inspectedWebView SUPPRESS_UNRETAINED_MEMBER;
```

## Default Value
`nil`。

## Discussion
`_WKInspectorWindow` の内部ヘッダで、`inspectedWebView` の `weak` プロパティに `SUPPRESS_UNRETAINED_MEMBER` を付けて警告を抑制するための宣言。実装は自動合成。

## References
- [`_WKInspectorWindowInternal.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorWindowInternal.h#L35)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
