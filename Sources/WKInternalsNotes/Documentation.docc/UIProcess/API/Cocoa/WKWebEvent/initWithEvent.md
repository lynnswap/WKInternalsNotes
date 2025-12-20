# ``WKInternalsNotes/WKWebEvent/initWithEvent(_:)``

`UIEvent` から `WebEvent` を構築する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithEvent:(UIEvent *)event;
```

## Discussion
ハードウェアキーボードイベントの場合は `UIPhysicalKeyboardEvent` をクローンし、キーコードや入力フラグを抽出して `WebEvent` を初期化する。ソフトウェアキー入力ではキーコードを 0 にし、入力フラグや修飾キーを 0 にして渡す。

## References
- [`WKWebEvent.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebEvent.h#L34)
- [`WKWebEvent.mm#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebEvent.mm#L38)
- [`WKWebEvent.mm#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebEvent.mm#L59)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
