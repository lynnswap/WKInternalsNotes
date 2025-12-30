# ``WKInternalsNotes/_WKElementAction/disabled``

アクションが無効かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL disabled;
```

## Default Value
`NO`。

## Discussion
初期化時に `disabled` を設定し、`uiActionForElementInfo:` では `UIMenuElementAttributesDisabled` を付与する。

## References
- [`_WKElementAction.h#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.h#L82)
- [`_WKElementAction.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L90)
- [`_WKElementAction.mm#L428`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L428)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
