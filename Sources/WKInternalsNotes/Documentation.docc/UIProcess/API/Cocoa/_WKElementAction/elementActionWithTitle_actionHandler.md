# ``WKInternalsNotes/_WKElementAction/elementActionWithTitle(_:actionHandler:)``

カスタムタイプのアクションを作成する。

## Objective-C Declaration
```objective-c
+ (instancetype)elementActionWithTitle:(NSString *)title actionHandler:(WKElementActionHandler)handler;
```

## Discussion
`_WKElementActionTypeCustom` として初期化し、`WKActionSheetAssistant` を無視する内部ハンドラを組み立てて保持する。

## References
- [`_WKElementAction.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.h#L72)
- [`_WKElementAction.mm#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L111)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
