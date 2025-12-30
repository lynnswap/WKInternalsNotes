# ``WKInternalsNotes/WKTimePickerViewController/initWithDelegate(_:)``

デリゲートを指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithDelegate:(id <WKQuickboardViewControllerDelegate>)delegate NS_DESIGNATED_INITIALIZER;
```

## Discussion
`[super initWithDelegate:delegate]` に委譲して初期化する。

## References
- [`WKTimePickerViewController.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTimePickerViewController.h#L32)
- [`WKTimePickerViewController.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTimePickerViewController.mm#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
