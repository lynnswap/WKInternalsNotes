# ``WKInternalsNotes/WKFormPeripheralBase/initWithView(_:control:)``

ビューとフォームコントロールを指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithView:(WKContentView *)view control:(RetainPtr<NSObject <WKFormControl>>&&)control NS_DESIGNATED_INITIALIZER;
```

## Discussion
`view` と `control` を保持して初期化する。

## References
- [`WKFormPeripheralBase.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.mm#L39)
- [`WKFormPeripheralBase.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.h#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
