# ``WKInternalsNotes/WKContentView/_keyboardWillShow()``

キーボード表示開始時の処理を行う。

## Objective-C Declaration
```objective-c
- (void)_keyboardWillShow;
```

## Discussion
キーボード表示待ちフラグを解除し、必要ならフォーカス要素の再表示ディファラを解決する。

## References
- [`WKContentViewInteraction.h#L771`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L771)
- [`WKContentViewInteraction.mm#L2883`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2883)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
