# ``WKInternalsNotes/WKBaseScrollView/_scrollingBehavior``

オーバーレイ領域のスクロール挙動を示す。

## Objective-C Declaration
```objective-c
@property (nonatomic) NSUInteger _scrollingBehavior;
```

## Default Value
未設定の場合は `0`。

## Discussion
OSS 側では本プロパティを設定する実装が見当たらず、テスト用のダンプで参照される。

## References
- [`WKBaseScrollView.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L62)
- [`WKWebViewTestingIOS.mm#L254`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L254)
- [`WKWebViewTestingIOS.mm#L255`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L255)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
