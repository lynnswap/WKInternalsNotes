# ``WKInternalsNotes/WKDatePickerViewController/initWithDelegate(_:)``

デリゲートを指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithDelegate:(id <WKQuickboardViewControllerDelegate>)delegate NS_DESIGNATED_INITIALIZER;
```

## Discussion
`[super initWithDelegate:delegate]` に委譲して初期化し、そのまま返す。

## References
- [`WKDatePickerViewController.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.h#L32)
- [`WKDatePickerViewController.mm#L224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerViewController.mm#L224)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
