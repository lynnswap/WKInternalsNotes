# ``WKInternalsNotes/WKContentView/_didStartProvisionalLoadForMainFrame()``

メインフレームの provisional load 開始時の処理を行う。

## Objective-C Declaration
```objective-c
- (void)_didStartProvisionalLoadForMainFrame;
```

## Discussion
ダブルタップ系ジェスチャをキャンセル/無効化し、画像解析などの状態をリセットする。

## References
- [`WKContentViewInteraction.h#L925`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L925)
- [`WKContentViewInteraction.mm#L6128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6128)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
