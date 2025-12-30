# ``WKInternalsNotes/WKVideoView/playerLayer``

プレイヤービューのレイヤーを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CALayer *playerLayer;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
`_playerView` の `layer` を返す。

## References
- [`WKVideoView.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKVideoView.h#L36)
- [`WKVideoView.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKVideoView.mm#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
