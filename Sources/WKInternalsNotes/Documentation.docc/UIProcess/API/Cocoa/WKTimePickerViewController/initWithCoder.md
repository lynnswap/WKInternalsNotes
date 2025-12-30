# ``WKInternalsNotes/WKTimePickerViewController/initWithCoder(_:)``

`NSCoder` 経由の初期化は不可。

## Objective-C Declaration
```objective-c
- (instancetype)initWithCoder:(NSCoder *)aDecoder NS_UNAVAILABLE;
```

## Discussion
`NS_UNAVAILABLE` 指定のため利用できず、`initWithDelegate:` を使用する。

## References
- [`WKTimePickerViewController.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTimePickerViewController.h#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
