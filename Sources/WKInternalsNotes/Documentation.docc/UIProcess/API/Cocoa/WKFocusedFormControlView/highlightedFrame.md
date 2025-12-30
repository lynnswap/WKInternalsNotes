# ``WKInternalsNotes/WKFocusedFormControlView/highlightedFrame``

ハイライト対象の矩形を保持し、マスクの切り抜きを更新する。

## Objective-C Declaration
```objective-c
@property (nonatomic) CGRect highlightedFrame;
```

## Default Value
`initWithFrame:delegate:` で `CGRectZero` に初期化される。

## Discussion
`setHighlightedFrame:` は `setHighlightedFrame:animated:NO` を呼び、`setHighlightedFrame:animated:` が `_highlightedFrame` を更新して `dimmingMaskLayer` の `path` を更新する（必要に応じてアニメーション）。

## References
- [`WKFocusedFormControlView.mm#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L65)
- [`WKFocusedFormControlView.mm#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L91)
- [`WKFocusedFormControlView.mm#L233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L233)
- [`WKFocusedFormControlView.mm#L298`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L298)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
