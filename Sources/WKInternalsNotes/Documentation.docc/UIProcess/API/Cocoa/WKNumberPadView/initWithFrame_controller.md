# ``WKInternalsNotes/WKNumberPadView/initWithFrame(_:controller:)``

ナンバーパッドビューを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(CGRect)frame controller:(WKNumberPadViewController *)controller NS_DESIGNATED_INITIALIZER;
```

## Discussion
`_controller` と `_contentView` を設定し、`_initKeypad` を呼んでキー配置を初期化する。

## References
- [`WKNumberPadView.h#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKNumberPadView.h#L77)
- [`WKNumberPadView.mm#L357`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKNumberPadView.mm#L357)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
