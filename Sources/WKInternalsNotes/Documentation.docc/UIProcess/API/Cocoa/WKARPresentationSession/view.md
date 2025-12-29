# ``WKInternalsNotes/WKARPresentationSession/view``

AR 表示用の `UIView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIView *view;
```

## Default Value
`loadView` で生成されるビュー。

## Discussion
`loadView` で画面サイズのビューを生成し、`_WKTransientGestureRecognizer` を追加して `self.view` に設定する。

## References
- [`WKARPresentationSession.mm#L244`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L244)
- [`WKARPresentationSession.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
