# ``WKInternalsNotes/WKContentView/_simulateTextEntered(_:)``

テキスト入力をシミュレートする。

## Objective-C Declaration
```objective-c
- (void)_simulateTextEntered:(NSString *)text;
```

## Discussion
フルスクリーンの入力リストや Quickboard が表示中であればそれぞれの入力経路に委譲し、該当しない場合は `insertText:` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L1032`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1032)
- [`WKContentViewInteraction.mm#L14452`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14452)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
