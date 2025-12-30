# ``WKInternalsNotes/WKFocusedFormControlView/dimmingMaskLayer``

`_dimmingView` の `mask` として使う `CAShapeLayer` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CAShapeLayer *dimmingMaskLayer;
```

## Default Value
`initWithFrame:delegate:` で `CAShapeLayer` を生成して `mask` に設定する。

## Discussion
`(CAShapeLayer *)[_dimmingView layer].mask` を返す。

## References
- [`WKFocusedFormControlView.mm#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L62)
- [`WKFocusedFormControlView.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
