# ``WKInternalsNotes/WKFormAccessoryView/autoFillButtonItem``

AutoFill ボタンの `UIBarButtonItem` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIBarButtonItem *autoFillButtonItem;
```

## Default Value
初期化時に生成されるが、非表示時に `nil` になる場合がある。

## Discussion
内部の `_autoFillButtonItem` をそのまま返す。`hideAutoFillButton` で非表示にすると `nil` になるケースがある。

## References
- [`WKFormAccessoryView.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.h#L53)
- [`WKFormAccessoryView.mm#L411`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.mm#L411)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
