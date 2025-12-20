# ``WKInternalsNotes/WKPasswordView/showInScrollView(_:)``

パスワード入力ビューをスクロールビューに表示する。

## Objective-C Declaration
```objective-c
- (void)showInScrollView:(UIScrollView *)scrollView;
```

## Discussion
スクロールビューのズームスケールやコンテンツサイズ、背景色を退避し、最小/最大ズームを 1 に固定してコンテンツサイズを自身のサイズに合わせる。背景色を `systemGroupedBackgroundColor` に変更したうえで、サブビューとして自身を追加する。

## References
- [`WKPasswordView.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.h#L33)
- [`WKPasswordView.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L90)
- [`WKPasswordView.mm#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L94)
- [`WKPasswordView.mm#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L100)
- [`WKPasswordView.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L106)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
