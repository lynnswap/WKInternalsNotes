# ``WKInternalsNotes/WKFocusedFormControlView/show(_:)``

ビューを表示状態にし、必要ならフェードインする。

## Objective-C Declaration
```objective-c
- (void)show:(BOOL)animated;
```

## Discussion
すでに `hidden == NO` なら何もしない。`hidden` を `NO` にし、`animated` が真なら `alpha` を 1 へアニメーション、それ以外は即時に設定する。

## References
- [`WKFocusedFormControlView.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L59)
- [`WKFocusedFormControlView.mm#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L140)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
