# ``WKInternalsNotes/WKSelectPicker/initWithView(_:)``

`WKContentView` を保持して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithView:(WKContentView *)view;
```

## Discussion
`_view` に `view` を保持し、`lastInteractionLocation` を `_interactionPoint` に保存する。

## References
- [`WKFormSelectPicker.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.h#L38)
- [`WKFormSelectPicker.mm#L507`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L507)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
