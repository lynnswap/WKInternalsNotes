# ``WKInternalsNotes/WKPageHostedModelView/remoteModelView``

リモートモデル表示用のビューを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, retain) UIView *remoteModelView;
```

## Discussion
既存のビューを取り外し、新しいビューを `_containerView` に追加する。フレームと autoresizing を合わせて設定する。

## References
- [`WKPageHostedModelView.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPageHostedModelView.h#L35)
- [`WKPageHostedModelView.mm#L201`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPageHostedModelView.mm#L201)
- [`WKPageHostedModelView.mm#L206`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPageHostedModelView.mm#L206)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
