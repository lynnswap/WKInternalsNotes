# ``WKInternalsNotes/WKFocusedFormControlView/nextHighlightedFrame``

次のフォーカス候補の矩形を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic) CGRect nextHighlightedFrame;
```

## Default Value
未設定の場合は `CGRectZero`。

## Discussion
`reloadData:` で delegate から取得して更新され、クラウン入力のスクロール計算に使われる。

## References
- [`WKFocusedFormControlView.mm#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L64)
- [`WKFocusedFormControlView.mm#L275`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L275)
- [`WKFocusedFormControlView.mm#L392`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L392)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
