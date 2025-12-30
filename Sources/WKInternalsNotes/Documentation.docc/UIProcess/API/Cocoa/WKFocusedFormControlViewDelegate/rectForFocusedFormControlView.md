# ``WKInternalsNotes/WKFocusedFormControlViewDelegate/rectForFocusedFormControlView(_:)``

現在のフォーカス矩形を返す。

## Objective-C Declaration
```objective-c
- (CGRect)rectForFocusedFormControlView:(WKFocusedFormControlView *)view;
```

## Discussion
`reloadData:` が `rectForFocusedFormControlView:` を呼び出してハイライト矩形を更新する。

## References
- [`WKFocusedFormControlView.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L37)
- [`WKFocusedFormControlView.mm#L272`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L272)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
