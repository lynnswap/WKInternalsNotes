# ``WKInternalsNotes/WKFocusedFormControlView/previousHighlightedFrame``

前のフォーカス候補の矩形を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic) CGRect previousHighlightedFrame;
```

## Default Value
未設定の場合は `CGRectZero`。

## Discussion
`reloadData:` で delegate から取得して更新され、クラウン入力のスクロール計算に使われる。

## References
- [`WKFocusedFormControlView.mm#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L63)
- [`WKFocusedFormControlView.mm#L274`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L274)
- [`WKFocusedFormControlView.mm#L387`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L387)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
