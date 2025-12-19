# ``WKInternalsNotes/WKContentView/_tryToHandlePressesEvent(_:)``

ハードウェアキーボードの押下イベントを先行処理する。

## Objective-C Declaration
```objective-c
- (BOOL)_tryToHandlePressesEvent:(UIPressesEvent *)event;
```

## Discussion
`event` がハードウェアキーボード由来で、`WKContentView` がファーストレスポンダーかつ編集対象外のときに `_inputPeripheral` へ `handleKeyEvent:` を委譲する。処理済みなら `YES` を返し、未処理なら初回のみ `reloadInputViews` を呼んで入力ビューを更新したうえで `NO` を返す。

## References
- [`WKContentViewInteraction.h#L1000`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1000)
- [`WKContentViewInteraction.mm#L7573`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7573)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
