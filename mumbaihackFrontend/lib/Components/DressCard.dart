import 'package:flutter/material.dart';

class DressCard extends StatelessWidget {
  const DressCard({
    super.key, required this.shirts, required this.index,
  });
  final List<String> shirts;
  final int index;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(
          vertical: 0.0, horizontal: 10),
      child: ClipRRect(
        borderRadius: BorderRadius.all(Radius.circular(30.0)),
        child: Container(
          height: 285,
          width: 360,
          child: Stack(
            fit: StackFit.expand,
            children: [
              Image(
                image: AssetImage(shirts[index]),
                fit: BoxFit.fill,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
