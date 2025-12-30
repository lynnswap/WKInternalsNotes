# ``WKInternalsNotes/WKVideoView/initWithFrame(_:playerView:)``

再生ビューを保持して初期化する。

## Objective-C Declaration
```objective-c
- (id)initWithFrame:(CGRect)frame playerView:(WebAVPlayerLayerView *)playerView;
```

## Discussion
`[super initWithFrame:]` が成功した場合、`_playerView` を保持して `addSubview:` で追加する。

## References
- [`WKVideoView.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKVideoView.h#L34)
- [`WKVideoView.mm#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKVideoView.mm#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
