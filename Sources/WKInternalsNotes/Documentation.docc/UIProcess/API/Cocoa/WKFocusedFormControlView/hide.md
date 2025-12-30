# ``WKInternalsNotes/WKFocusedFormControlView/hide(_:)``

ビューを非表示にし、必要ならフェードアウトする。

## Objective-C Declaration
```objective-c
- (void)hide:(BOOL)animated;
```

## Discussion
すでに `hidden == YES` なら何もしない。`animated` が偽なら `alpha = 0` と `hidden = YES` を即時設定し、真なら `alpha` を 0 へアニメーションして完了時に `hidden = YES` を設定する。

## References
- [`WKFocusedFormControlView.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L60)
- [`WKFocusedFormControlView.mm#L157`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L157)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
