# ``WKInternalsNotes/_WKElementAction/_elementActionWithType(_:title:actionHandler:)``

内部用にハンドラをラップしてアクションを作成する。

## Objective-C Declaration
```objective-c
+ (instancetype)_elementActionWithType:(_WKElementActionType)type title:(NSString *)title actionHandler:(WKElementActionHandler)actionHandler;
```

## Discussion
`WKActionSheetAssistant` を無視するラッパを生成し、`_initWithTitle` で `assistant:nil` のアクションを返す。

## References
- [`_WKElementActionInternal.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementActionInternal.h#L37)
- [`_WKElementAction.mm#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L132)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
