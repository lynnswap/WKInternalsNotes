# ``WKInternalsNotes/_WKInspectorWindow/SUPPRESS_UNRETAINED_MEMBER``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, readwrite, weak) WKWebView *inspectedWebView SUPPRESS_UNRETAINED_MEMBER;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKInspectorWindowInternal.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorWindowInternal.h#L35)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
