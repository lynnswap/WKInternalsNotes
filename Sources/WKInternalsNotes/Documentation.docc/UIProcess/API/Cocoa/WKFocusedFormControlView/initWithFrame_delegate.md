# ``WKInternalsNotes/WKFocusedFormControlView/initWithFrame(_:delegate:)``

フォーカス用のオーバーレイ UI を構築して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(CGRect)frame delegate:(id <WKFocusedFormControlViewDelegate>)delegate;
```

## Discussion
`_delegate` と `_highlightedFrame` を設定し、`_dimmingView` とその `mask` を生成する。送信/キャンセルボタンやタップジェスチャを設定し、サブビューを追加して初期状態を整える。

## References
- [`WKFocusedFormControlView.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.h#L54)
- [`WKFocusedFormControlView.mm#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFocusedFormControlView.mm#L85)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
