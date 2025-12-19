# ``WKInternalsNotes/WKContentView/_keyboardDidShow()``

キーボード表示完了後の処理を行う。

## Objective-C Declaration
```objective-c
- (void)_keyboardDidShow;
```

## Discussion
メインループでフォーカス要素の再表示ディファラを解決し、必要に応じてコンテキストメニュー位置を再調整する。

## References
- [`WKContentViewInteraction.h#L772`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L772)
- [`WKContentViewInteraction.mm#L2891`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2891)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
